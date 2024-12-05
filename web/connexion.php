<?php
// Include the database connection
include 'db_connect.php';

// Start the session to track user login status
session_start();

// Initialize an error message variable
$error = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $login = $_POST['login'];
    $password = $_POST['password'];

    // Check if login and password are provided
    if (!empty($login) && !empty($password)) {
        try {
            // Use PDO to connect to the database (update with database configuration)
            $pdo = new PDO('mysql:host=db;dbname=passoire', 'passoire', 'jonathan');
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Use a parameterized query to prevent SQL injection
            $stmt = $pdo->prepare('SELECT id, pwhash FROM users WHERE login = :login');
            $stmt->bindParam(':login', $login, PDO::PARAM_STR);
            $stmt->execute();
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user) {
                // Verify the password using password_verify
                if (password_verify($password, $user['pwhash'])) {
                    // Password verification successful
                    $_SESSION['user_id'] = $user['id'];
                    session_regenerate_id(true); // Prevent session fixation attacks
                    header('Location: index.php'); // Redirect to the homepage after successful login
                    exit();
                } else {
                    // Password doesn't match
                    $error = 'Invalid password. Please try again.';
                }
            } else {
                // User not found
                $error = 'Invalid login. Please try again.';
            }
        } catch (PDOException $e) {
            // Database error
            $error = 'Database error: ' . $e->getMessage();
        }
    } else {
        $error = 'Please fill in both fields.';
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Passoire: A simple file hosting server</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="./style/w3.css">
    <link rel="stylesheet" href="./style/w3-theme-blue-grey.css">
    <link rel="stylesheet" href="./style/css/fontawesome.css">
    <link href="./style/css/brands.css" rel="stylesheet" />
    <link href="./style/css/solid.css" rel="stylesheet" />
    <style>
        html, body, h1, h2, h3, h4, h5 {font-family: "Open Sans", sans-serif}
        .center-c {
            margin-bottom: 25px;
            padding-bottom: 25px;
        }
    </style>
</head>
<body class="w3-theme-l5">
<?php include 'navbar.php'; ?>

<!-- Page Container -->
<div class="w3-container w3-content" style="max-width:1400px;margin-top:80px">
    <!-- The Grid -->
    <div class="w3-row">
        <div class="w3-col m12">
            <div class="w3-card w3-round">
                <div class="w3-container w3-center center-c">
                    <h2>Login</h2>

                    <?php if ($error): ?>
                        <p class="error"><?php echo $error; ?></p>
                    <?php endif; ?>

                    <form action="connexion.php" method="post">
                        <input type="text" class="w3-border w3-padding w3-margin" name="login" placeholder="Login" required><br />
                        <input type="password" class="w3-border w3-padding w3-margin" name="password" placeholder="Password" required><br />
                        <button type="submit" class="w3-button w3-theme w3-margin">Login</button><br />
                    </form>
                    
                    <p>Don't have a login yet? <a href="signup.php"> Sign up here!</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
