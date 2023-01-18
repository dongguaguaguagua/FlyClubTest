<?php
/**
 * Plugin installation functions
 *
 * @package YITH\CatalogMode
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly.
}

if ( defined( 'YWCTM_PREMIUM' ) && YWCTM_PREMIUM ) {

	if ( '' !== (string) get_option( 'ywctm_enable_plugin' ) ) {
		include_once YWCTM_DIR . 'includes/actions/update-2.0.0/ywctm-update-premium.php';
	} else {
		include_once YWCTM_DIR . 'includes/actions/update-2.0.0/ywctm-default-buttons.php';
	}
} else {
	if ( '' !== get_option( 'ywctm_enable_plugin' ) ) {
		include_once YWCTM_DIR . 'includes/actions/update-2.0.0/ywctm-update.php';
	} else {
		update_option( 'ywctm_update_version', YWCTM_VERSION );
	}
}
