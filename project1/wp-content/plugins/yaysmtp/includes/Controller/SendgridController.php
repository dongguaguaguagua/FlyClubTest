<?php
namespace YaySMTP\Controller;

use YaySMTP\Helper\LogErrors;
use YaySMTP\Helper\Utils;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
class SendgridController {
	private $headers = array();
	private $body    = array();
	private $smtper;

	public function getApiKey() {
		$apiKey          = '';
		$yaysmtpSettings = Utils::getYaySmtpSetting();
		if ( ! empty( $yaysmtpSettings ) && is_array( $yaysmtpSettings ) ) {
			if ( ! empty( $yaysmtpSettings['sendgrid'] ) && ! empty( $yaysmtpSettings['sendgrid']['api_key'] ) ) {
				$apiKey = $yaysmtpSettings['sendgrid']['api_key'];
			}
		}
		return $apiKey;
	}

	public function __construct( $phpmailer ) {
		// Set wp_mail_from && wp_mail_from_name - start
		$currentFromEmail = Utils::getCurrentFromEmail();
		$currentFromName  = Utils::getCurrentFromName();
		$from_email       = apply_filters( 'wp_mail_from', $currentFromEmail );
		$from_name        = apply_filters( 'wp_mail_from_name', $currentFromName );
		if ( Utils::getForceFromEmail() == 1 ) {
			$from_email = $currentFromEmail;
		}
		if ( Utils::getForceFromName() == 1 ) {
			$from_name = $currentFromName;
		}
		$phpmailer->setFrom( $from_email, $from_name, false );
		// Set wp_mail_from && wp_mail_from_name - end

		$this->smtper                   = $phpmailer;
		$this->headers['content-type']  = 'application/json';
		$this->headers['Authorization'] = 'Bearer ' . $this->getApiKey();

		$headers = $phpmailer->getCustomHeaders();
		foreach ( $headers as $head ) {
			$nameHead  = isset( $head[0] ) ? $head[0] : false;
			$valueHead = isset( $head[1] ) ? $head[1] : false;
			if ( ! empty( $nameHead ) ) {
				$headersData              = isset( $this->body['headers'] ) ? (array) $this->body['headers'] : array();
				$headersData[ $nameHead ] = $valueHead;

				$this->body = array_merge( $this->body, array( 'headers' => $headersData ) );
			}
		}

		$this->body = array_merge( $this->body, array( 'subject' => $phpmailer->Subject ) );

		if ( ! empty( $phpmailer->FromName ) ) {
			$dataFrom['name'] = $phpmailer->FromName;
		}
		$dataFrom['email'] = $phpmailer->From;

		$this->body = array_merge( $this->body, array( 'from' => $dataFrom ) );

		$toAddresses = $phpmailer->getToAddresses();
		if ( ! empty( $toAddresses ) && is_array( $toAddresses ) ) {
			$dataRecips['to'] = array();
			foreach ( $toAddresses as $toEmail ) {
				$address        = isset( $toEmail[0] ) ? $toEmail[0] : false;
				$name           = isset( $toEmail[1] ) ? $toEmail[1] : false;
				$arrTo          = array();
				$arrTo['email'] = $address;
				if ( ! empty( $name ) ) {
					$arrTo['name'] = $name;
				}
				$dataRecips['to'][] = $arrTo;
			}
		}

		$ccAddresses = $phpmailer->getCcAddresses();
		if ( ! empty( $ccAddresses ) && is_array( $ccAddresses ) ) {
			$dataRecips['cc'] = array();
			foreach ( $ccAddresses as $ccEmail ) {
				$address        = isset( $ccEmail[0] ) ? $ccEmail[0] : false;
				$name           = isset( $ccEmail[1] ) ? $ccEmail[1] : false;
				$arrCc          = array();
				$arrCc['email'] = $address;
				if ( ! empty( $name ) ) {
					$arrCc['name'] = $name;
				}
				$dataRecips['cc'][] = $arrCc;
			}
		}

		$bccAddresses = $phpmailer->getBccAddresses();
		if ( ! empty( $bccAddresses ) && is_array( $bccAddresses ) ) {
			$dataRecips['bcc'] = array();
			foreach ( $bccAddresses as $bccEmail ) {
				$address         = isset( $bccEmail[0] ) ? $bccEmail[0] : false;
				$name            = isset( $bccEmail[1] ) ? $bccEmail[1] : false;
				$arrBcc          = array();
				$arrBcc['email'] = $address;
				if ( ! empty( $name ) ) {
					$arrBcc['name'] = $name;
				}
				$dataRecips['bcc'][] = $arrBcc;
			}
		}

		if ( ! empty( $dataRecips ) ) {
			$this->body = array_merge( $this->body, array( 'personalizations' => array( $dataRecips ) ) );
		}

		if ( 'text/plain' === $phpmailer->ContentType ) {
			$content              = $phpmailer->Body;
			$dataContent['type']  = 'text/plain';
			$dataContent['value'] = $content;
			$this->body           = array_merge( $this->body, array( 'content' => array( $dataContent ) ) );
		} else {
			$content     = array(
				'text' => $phpmailer->AltBody,
				'html' => $phpmailer->Body,
			);
			$dataContent = array();
			foreach ( $content as $type => $body ) {
				if ( empty( $body ) ) {
					continue;
				}

				if ( 'html' === $type ) {
					$ctype = 'text/html';
				} else {
					$ctype = 'text/plain';
				}

				$dataContent[] = array(
					'type'  => $ctype,
					'value' => $body,
				);
			}

			$this->body = array_merge( $this->body, array( 'content' => $dataContent ) );
		}

		// Reply to
		$replyToAddresses = $phpmailer->getReplyToAddresses();
		if ( ! empty( $replyToAddresses ) ) {
			$dataReplyTo = array();

			foreach ( $replyToAddresses as $emailReplys ) {
				if ( empty( $emailReplys ) || ! is_array( $emailReplys ) ) {
					continue;
				}

				$addrReplyTo = isset( $emailReplys[0] ) ? $emailReplys[0] : false;
				$nameReplyTo = isset( $emailReplys[1] ) ? $emailReplys[1] : false;

				if ( ! filter_var( $addrReplyTo, FILTER_VALIDATE_EMAIL ) ) {
					continue;
				}

				$dataReplyTo['email'] = $addrReplyTo;
				if ( ! empty( $name ) ) {
					$dataReplyTo['name'] = $nameReplyTo;
				}
			}

			if ( ! empty( $dataReplyTo ) ) {
				$this->body = array_merge( $this->body, array( 'reply_to' => $dataReplyTo ) );
			}
		}

		// Set attachments.
		$attachments = $phpmailer->getAttachments();
		if ( ! empty( $attachments ) ) {
			$dataAttachments = array();
			$allowedAttach   = array( 'xlsx', 'xls', 'ods', 'docx', 'docm', 'doc', 'csv', 'pdf', 'txt', 'gif', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'rtf', 'bmp', 'cgm', 'css', 'shtml', 'html', 'htm', 'zip', 'xml', 'ppt', 'pptx', 'tar', 'ez', 'ics', 'mobi', 'msg', 'pub', 'eps', 'odt', 'mp3', 'm4a', 'm4v', 'wma', 'ogg', 'flac', 'wav', 'aif', 'aifc', 'aiff', 'mp4', 'mov', 'avi', 'mkv', 'mpeg', 'mpg', 'wmv' );
			foreach ( $attachments as $attach ) {
				$attachFile = false;
				try {
					if ( is_file( $attach[0] ) && is_readable( $attach[0] ) ) {
						$extension = pathinfo( $attach[0], PATHINFO_EXTENSION );
						if ( in_array( $extension, $allowedAttach, true ) ) {
							  $attachFile = file_get_contents( $attach[0] );
						}
					}
				} catch ( \Exception $except ) {
					$attachFile = false;
				}

				if ( false === $attachFile ) {
					continue;
				}

				$filetype = str_replace( ';', '', trim( $attach[4] ) );

				$dataAttachments[] = array(
					'content'     => base64_encode( $attachFile ),
					'type'        => $filetype,
					'filename'    => empty( $attach[2] ) ? 'file-' . wp_hash( microtime() ) . '.' . $filetype : trim( $attach[2] ),
					'disposition' => in_array( $attach[6], array( 'inline', 'attachment' ), true ) ? $attach[6] : 'attachment',
					'content_id'  => empty( $attach[7] ) ? '' : trim( (string) $attach[7] ),
				);
			}

			if ( ! empty( $dataAttachments ) ) {
				$this->body = array_merge( $this->body, array( 'attachments' => $dataAttachments ) );
			}
		}
	}

	public function send() {
		$response = wp_safe_remote_post(
			'https://api.sendgrid.com/v3/mail/send',
			array(
				'httpversion' => '1.1',
				'blocking'    => true,
				'headers'     => $this->headers,
				'body'        => wp_json_encode( $this->body ),
				'timeout'     => ini_get( 'max_execution_time' ) ? (int) ini_get( 'max_execution_time' ) : 30,
			)
		);

		if ( is_wp_error( $response ) ) {
			$errors = $response->get_error_messages();
			foreach ( $errors as $error ) {
				LogErrors::setErr( $error );
			}
			return;
		}

		$emailTo     = array();
		$toAddresses = $this->smtper->getToAddresses();
		if ( ! empty( $toAddresses ) && is_array( $toAddresses ) ) {
			foreach ( $toAddresses as $toEmail ) {
				if ( ! empty( $toEmail[0] ) ) {
					$emailTo[] = $toEmail[0];
				}
			}
		}

		if ( $this->smtper->ContentType ) {
			$dataLogsDB = array(
				'subject'      => $this->smtper->Subject,
				'email_from'   => $this->smtper->From,
				'email_to'     => $emailTo, // require is array
				'mailer'       => 'Sendgrid',
				'date_time'    => current_time( 'mysql' ),
				'status'       => 0, // 0: false, 1: true, 2: waiting
				'content_type' => $this->smtper->ContentType,
				'body_content' => $this->smtper->Body,
			);
		}

		$sent = false;
		if ( ! empty( $response['response'] ) && ! empty( $response['response']['code'] ) ) {
			$code        = (int) $response['response']['code'];
			$codeSucArrs = array( 200, 201, 202, 203, 204, 205, 206, 207, 208, 300, 301, 302, 303, 304, 305, 306, 307, 308 );
			if ( ! in_array( $code, $codeSucArrs ) && ! empty( $response['response'] ) ) {
				$error   = $response['response'];
				$message = '';
				if ( ! empty( $error ) ) {
					$message = '[' . $error['code'] . ']: ' . $error['message'];
				}
				LogErrors::clearErr();
				LogErrors::setErr( 'Mailer: sendgrid' );
				LogErrors::setErr( $message );

				$dataLogsDB['date_time']    = current_time( 'mysql' );
				$dataLogsDB['reason_error'] = $message;
				Utils::insertEmailLogs( $dataLogsDB );
			} else {
				$sent = true;
				LogErrors::clearErr();

				$dataLogsDB['date_time'] = current_time( 'mysql' );
				$dataLogsDB['status']    = 1;
				Utils::insertEmailLogs( $dataLogsDB );
			}
		}
		return $sent;
	}
}
