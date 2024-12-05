<?php

// Database credentials
$host = getenv('DB_HOST') ?: 'db';
$dbname = getenv('DB_NAME') ?: 'passoire';
$username = getenv('DB_USER') ?: 'passoire';
$password = getenv('DB_PASSWORD') ?: 'jonathan';

$dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";
try{
    

    $pdoatts = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch results as associative arrays
        PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation for prepared statements
    ];

    $conn = new PDO($dsn, $username, $password, $pdoatts);

    $conn->beginTransaction();
    

}catch(PDOException $e) {
    if ($pdo->inTransaction()) {

        $pdo->rollBack();
        echo nl2br("\nErrors found" . $e->getMessage());
    }
}
/* TODO: Replace old SQL connector with modern PDO and prepared statements.*/
?>

