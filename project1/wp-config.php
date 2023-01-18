<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('WP_CACHE', true);
define( 'WPCACHEHOME', __dir__ .'/wp-content/plugins/wp-super-cache/' );
define( 'DB_NAME', 'database' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost:8080' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'nsjnvdgh1rximsnqbymfdenq1fszjlu1khzzyyjpnon2txlxvpfirtksbwx3cpcq' );
define( 'SECURE_AUTH_KEY',  'ibfmgkc98vwdnmwly3awpisnzydun3i0dpoqtbye9gtgfhcovz0bgfqviljojzfj' );
define( 'LOGGED_IN_KEY',    'm8cjipmtbsczn2q16urd6u3srbmr3w7bwmiimqonlmqs03fxh2qo6jhysdpyscj6' );
define( 'NONCE_KEY',        'o5sp6jor6clgpzswntvdwobi3px1gff24ddsiskt1sxrkfrhzelwiswgzoap3nvl' );
define( 'AUTH_SALT',        'yjero8srp2yyw6jbo7veophwjlat5z7rjcwlsvfudqhcsnnpbl2thgsnub8cavha' );
define( 'SECURE_AUTH_SALT', '7b98vjfsn9l24rtdxdfi5ccmizryuu6ikjeqefq6psdbvjguoksmlrbku9pw8gox' );
define( 'LOGGED_IN_SALT',   'q9qxf4wmpjen0mpowu1bvjntey7apspty40h47etkzqwaoz9r4skrn2ksdyr4s4d' );
define( 'NONCE_SALT',       'rnvindukte1qdzf9dzsyrfbkgh6qvrbgcdne7hdsjahu5ld0aixyqakoygmtankv' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wpp7_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __dir__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
