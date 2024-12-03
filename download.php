<?php
// Assuming the file is located outside the web root
$file = '/passoire/web/uploads/secret';
$valid_tokens = ['abc123', 'def456', 'ghi789']; 

$token = $_GET['token'] ?? '';

if (in_array($token, $valid_tokens) && file_exists($file)) {
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="secret"');
    readfile($file); 
    exit;
} else {
    http_response_code(403);
    echo "Access denied. Invalid or missing token.";
}
?>
