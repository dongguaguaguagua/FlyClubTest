<?php
use YaySMTP\Helper\Utils;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$templatePart = YAY_SMTP_PLUGIN_PATH . 'includes/Views/template-part';

$yaysmtp_mail_report_choose = 'no';
$yaysmtp_mail_report_type   = 'weekly';
$has_mail_fallback          = 'no';
$fallback_force_from_email  = 'yes';
$fallback_force_from_name   = 'no';
$fallback_host              = '';
$fallback_encryption        = 'tls';
$fallback_port              = '';
$fallback_auth              = 'yes';
$fallback_user              = '';
$fallback_pass              = '';
$uninstall_flag             = 'no';

if ( ! empty( $params['params'] ) ) {
	$settings = $params['params'];
	if ( isset( $settings['mail_report_choose'] ) ) {
		$yaysmtp_mail_report_choose = $settings['mail_report_choose'];
	}
	if ( ! empty( $settings['mail_report_type'] ) ) {
		$yaysmtp_mail_report_type = $settings['mail_report_type'];
	}
	if ( isset( $settings['fallback_has_setting_mail'] ) ) {
		$has_mail_fallback = $settings['fallback_has_setting_mail'];
	}
	if ( isset( $settings['fallback_force_from_email'] ) ) {
		$fallback_force_from_email = $settings['fallback_force_from_email'];
	}
	if ( isset( $settings['fallback_force_from_name'] ) ) {
		$fallback_force_from_name = $settings['fallback_force_from_name'];
	}
	if ( isset( $settings['fallback_host'] ) ) {
		$fallback_host = $settings['fallback_host'];
	}
	if ( isset( $settings['fallback_auth_type'] ) ) {
		$fallback_encryption = $settings['fallback_auth_type'];
	}
	if ( isset( $settings['fallback_port'] ) ) {
		$fallback_port = $settings['fallback_port'];
	}
	if ( isset( $settings['fallback_auth'] ) ) {
		$fallback_auth = $settings['fallback_auth'];
	}
	if ( isset( $settings['fallback_smtp_user'] ) ) {
		$fallback_user = $settings['fallback_smtp_user'];
	}
	if ( isset( $settings['fallback_smtp_pass'] ) ) {
		$fallback_pass = Utils::decrypt( $settings['fallback_smtp_pass'], 'smtppass' );
	}
	if ( isset( $settings['uninstall_flag'] ) ) {
		$uninstall_flag = $settings['uninstall_flag'];
	}
}

$styleShowHidePage = 'none';
$mainTab           = Utils::getParamUrl( 'page' );
$childTab          = Utils::getParamUrl( 'tab' );
if ( 'yaysmtp' === $mainTab && 'additional-setting' === $childTab ) {
	$styleShowHidePage = 'block';
}
?>

<div class="yay-smtp-wrap yaysmtp-additional-settings-wrap" style="display:<?php echo esc_attr( $styleShowHidePage ); ?>">
  <div class="yay-button-first-header">
	<div class="yay-button-header-child-left">
	  <span class="dashicons dashicons-arrow-left-alt"></span>
	  <span><a class="mail-setting-redirect">Back to Settings page</a></span>
	</div>
  </div>
  <div class="yay-smtp-card">
	<div class="yay-smtp-card-header">
	  <div class="yay-smtp-card-title-wrapper">
		<h3 class="yay-smtp-card-title yay-smtp-card-header-item">
		  <?php echo esc_html__( 'Additional Settings', 'yay-smtp' ); ?>
		</h3>
	  </div>
	</div>
	<div class="yay-smtp-card-body">
	  <div class="setting-mail-report setting-el">
		<div class="setting-label">
		  <label for="yaysmtp_addition_setts_report_cb"><?php echo esc_html__( 'Email Notifications', 'yay-smtp' ); ?></label>
		</div>
		<div class="yaysmtp-addition-setts-report-cb">
		  <div class="additional-settings-title"><input id="yaysmtp_addition_setts_report_cb" type="checkbox" <?php echo 'yes' === $yaysmtp_mail_report_choose ? 'checked' : ''; ?>/></div>
		  <div>
			<label for="yaysmtp_addition_setts_report_cb">
			  <?php echo esc_html__( 'Receive SMTP email delivery summary via email.', 'yay-smtp' ); ?>
			</label>
		  </div>
		</div>
		<div class="yaysmtp-addition-setts-report-detail">
		  <label class="radio-setting">
			<input type="radio" id="yaysmtp_addition_setts_report_weekly" name="yaysmtp_addition_setts_mail_report"  value="weekly" <?php echo 'weekly' === $yaysmtp_mail_report_type ? 'checked' : ''; ?>>
			<?php echo esc_html__( 'Weekly', 'yay-smtp' ); ?>
		  </label>
		  <label class="radio-setting">
			<input type="radio" id="yaysmtp_addition_setts_report_monthly" name="yaysmtp_addition_setts_mail_report" value="monthly" <?php echo 'monthly' === $yaysmtp_mail_report_type ? 'checked' : ''; ?>>
			<?php echo esc_html__( 'Monthly', 'yay-smtp' ); ?>
		  </label>
		</div>
	  </div>
	  <div class="setting-el">
		<div class="setting-label">
		  <label for="yaysmtp_addition_setts_uninstall"><?php echo esc_html__( 'Remove All YaySMTP Data', 'yay-smtp' ); ?></label>
		</div>
		<div class="yaysmtp-addition-setts-report-cb">
		  <div class="additional-settings-title"><input id="yaysmtp_addition_setts_uninstall" type="checkbox" <?php echo 'yes' === $uninstall_flag ? 'checked' : ''; ?>/></div>
		  <div>
			<label for="yaysmtp_addition_setts_uninstall">
			  <?php echo esc_html__( 'Remove ALL YaySMTP data when uninstall plugin. All settings will be unrecoverable (Be very careful when choosing this setting).', 'yay-smtp' ); ?>
			</label>
		  </div>
		</div>
	  </div>
	  <div class="setting-mail-fallback setting-el">
		<div class="setting-label">
		  <label for="yaysmtp_setting_mail_fallback"><?php echo esc_html__( 'Fallback Carrier', 'yay-smtp' ); ?></label>
		</div>
		<div class="yaysmtp-setting-mail-fallback-wrap">
		  <div class="mail-fallback-title"><input id="yaysmtp_setting_mail_fallback" class="yaysmtp-setting-mail-fallback" type="checkbox" <?php echo 'yes' === $has_mail_fallback ? 'checked' : ''; ?>/></div>
		  <div>
			<label for="yaysmtp_setting_mail_fallback">
			  <?php echo esc_html__( 'Configure a secondary email service provider to send WordPress emails. Automatically used after the first mailer has 3 failed attempts.', 'yay-smtp' ); ?>
			</label>
		  </div>
		</div>

		<div class="yaysmtp-fallback-setting-detail-wrap" style="display: <?php echo 'yes' === $has_mail_fallback ? 'flex' : 'none'; ?>">
		  <div class="yaysmtp-fallback-setting-opt-wrap">
			<div class="yay-smtp-card-header yaysmtp-fallback-setting-detail-header">
			  <div class="title-wrap"><?php echo esc_html__( 'Fallback PHPMailer Settings', 'yay-smtp' ); ?></div>
			  <div class="button-wrap">
				<button type="button" class="yay-smtp-button panel-tab-btn send-test-fallback-mail-panel">
				  <svg viewBox="64 64 896 896" data-icon="mail" width="15" height="15" fill="currentColor" aria-hidden="true" focusable="false" class=""><path d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32zm-40 110.8V792H136V270.8l-27.6-21.5 39.3-50.5 42.8 33.3h643.1l42.8-33.3 39.3 50.5-27.7 21.5zM833.6 232L512 482 190.4 232l-42.8-33.3-39.3 50.5 27.6 21.5 341.6 265.6a55.99 55.99 0 0 0 68.7 0L888 270.8l27.6-21.5-39.3-50.5-42.7 33.2z"></path></svg>
				  <span class="text">Send Test Fallback Email</span>
				</button>
			  </div>
			</div>
			<div class="yay-smtp-card-body">
			  <div>
				<div class="yaysmtp-component-title"> Step 1: Enter Email From </div>

				<div class="yaysmtp-component-content"> 
				  <div class="setting-from-email">
					<div class="setting-label">
					  <label for="yaysmtp_fallback_from_email">From Email</label>
					</div>
					<div>
					  <input type="text" id="yaysmtp_fallback_from_email" value="<?php echo esc_attr( Utils::getCurrentFromEmailFallback() ); ?>" />
					  <p class="error-message-email" style="display:none"></p>
					  <p class="setting-description">
						The email displayed in the "From" field.
					  </p>
					  <div>
						<input
						  id="yaysmtp_fallback_force_from_email"
						  type="checkbox"
						  <?php echo 'yes' === $fallback_force_from_email ? 'checked' : ''; ?>
						/>
						<label for="yaysmtp_fallback_force_from_email">Force From Email</label>
						<div class="yay-tooltip icon-tootip-wrap">
						  <span class="icon-inst-tootip"></span>
						  <span class="yay-tooltiptext yay-tooltip-bottom"><?php echo esc_html__( 'Always send emails with the above From Email address, overriding other plugins settings.', 'yay-smtp' ); ?></span>
						</div>
					  </div>
					</div>
				  </div>
				  <div class="setting-from-name">
					<div class="setting-label">
					  <label for="yaysmtp_fallback_from_name">From Name</label>
					</div>
					<div>
					  <input type="text" id="yaysmtp_fallback_from_name" value="<?php echo esc_attr( Utils::getCurrentFromNameFallback() ); ?>"/>
					  <p class="setting-description">
						The name displayed in emails
					  </p>
					  <div>
						<input
						  id="yaysmtp_fallback_force_from_name"
						  type="checkbox"
						  <?php echo 'yes' === $fallback_force_from_name ? 'checked' : ''; ?>
						/>
						<label for="yaysmtp_fallback_force_from_name">Force From Name</label>
						<div class="yay-tooltip icon-tootip-wrap">
						  <span class="icon-inst-tootip"></span>
						  <span class="yay-tooltiptext yay-tooltip-bottom"><?php echo esc_html__( 'Always send emails with the above From Name, overriding other plugins settings.', 'yay-smtp' ); ?></span>
						</div>
					  </div>
					</div>
				  </div>
				</div> 
			  </div>
			  

			  <div>
				<div class="yaysmtp-component-title"> Step 2: Config for SMTP</div>
				<div class="yaysmtp-component-content"> 
					<div class="setting-el">
					  <div class="setting-label">
						<label for="yaysmtp_fallback_host">SMTP Host</label>
					  </div>
					  <div>
						<input type="text" id="yaysmtp_fallback_host" value="<?php echo esc_attr( $fallback_host ); ?>">
					  </div>
					</div>
					<div class="setting-el">
					  <div class="setting-label">
						<label for="yaysmtp_fallback_encryption_tls">Encryption Type</label>
					  </div>
					  <div>
						<label class="radio-setting">
						  <input type="radio" id="yaysmtp_fallback_encryption_ssl" name="yaysmtp-fallback-encryption" value="ssl" <?php echo 'ssl' === $fallback_encryption ? 'checked' : ''; ?>>
						  SSL
						</label>
						<label class="radio-setting">
						  <input type="radio" id="yaysmtp_fallback_encryption_tls" name="yaysmtp-fallback-encryption" value="tls" <?php echo 'tls' === $fallback_encryption ? 'checked' : ''; ?>>
						  TLS
						</label>
						<p class="setting-description">
						  TLS is the recommended option if your SMTP provider supports it.
						</p>
					  </div>
					</div>
					<div class="setting-el">
					  <div class="setting-label">
						<label for="yaysmtp_fallback_port">SMTP Port</label>
					  </div>
					  <div>
						<input type="number" id="yaysmtp_fallback_port" value="<?php echo esc_attr( $fallback_port ); ?>">
						<p class="setting-description">
						  Port of your mail server. Usually is 25, 465, 587
						</p>
					  </div>
					</div>
					<div class="setting-el">
					  <div class="setting-label">
						<label for="yaysmtp_fallback_auth">SMTP Authentication</label>
					  </div>
					  <div>
						<label class="switch">
						  <input type="checkbox" id="yaysmtp_fallback_auth" <?php echo 'yes' === $fallback_auth ? 'checked' : ''; ?>>
						  <span class="slider round"></span>
						</label>
						<label class="toggle-label">
						  <span class="setting-toggle-fallback-checked">ON</span>
						  <span class="setting-toggle-fallback-unchecked">OFF</span>
						</label>
					  </div>
					</div>
					<div class="yaysmtp_fallback_auth_det" style="display: <?php echo 'yes' === $fallback_auth ? 'block' : 'none'; ?>">
					  <div class="setting-el">
						<div class="setting-label">
						  <label for="yaysmtp_fallback_smtp_user">SMTP Username</label>
						</div>
						<div>
						  <input type="text" id="yaysmtp_fallback_smtp_user" value="<?php echo esc_attr( $fallback_user ); ?>">
						</div>
					  </div>
					  <div class="setting-el">
						<div class="setting-label">
						  <label for="yaysmtp_fallback_smtp_pass">SMTP Password</label>
						</div>
						<div>
						  <input type="password" spellcheck="false" id="yaysmtp_fallback_smtp_pass" value="<?php echo esc_attr( $fallback_pass ); ?>">
						</div>
					  </div>
					</div>
				  </div>
				  
				</div>
			</div>
		  </div>

		  <!-- Send test fallback mail drawer - start -->
		  <?php Utils::getTemplatePart( $templatePart, 'send-test-mail-fallback', array() ); ?>
		  <!-- Send test fallback mail drawer - end -->
		</div>
	  </div>
	</div>
  </div>
  <div>
	<button type="button" class="yay-smtp-button yaysmtp-additional-settings-btn"><?php echo esc_html__( 'Save Changes', 'yay-smtp' ); ?></button>
  </div>
</div>





