
<?php
/**
 * Web Tier Proxy Script
 * Forwards requests from the public web tier to the internal ALB (app tier)
 */

$internal_alb = "http://<internal-alb-dns-name>";
$response = file_get_contents($internal_alb . "/query");
header('Content-Type: application/json');
echo $response;
?>

