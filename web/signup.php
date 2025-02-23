<?php
// Include database connection
include 'db_connect.php';

// Function to hash passwords
// function hashPassword($password) {
//     return sha1($password);
// }
// Function to hash passwords with salt
function hashPasswordWithSalt($password, $salt) {
    return hash('sha256', $salt . $password); // 使用 SHA-256 生成哈希
}
// Function to generate a random salt
function generateSalt() {
    return bin2hex(random_bytes(16)); // 生成16字节（32字符）的随机盐
}


// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $login = $_POST['login'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password_confirm = $_POST['password_confirm'];

    // Validate passwords
    if ($password !== $password_confirm) {
        $error = "<p class=\"error\">Passwords do not match. Please try again.</p>";
    } else {
        // Check if the login or email already exists
        
        // Check if the login or email already exists
        $sql = "SELECT id FROM users WHERE login = :login OR email = :email";
        $qr = $conn->prepare($sql);
        $qr->bindParam(':login', $login, PDO::PARAM_STR);
        $qr->bindParam(':email', $email, PDO::PARAM_STR);
         // Check for errors during execution
       
        $qr->fetch(PDO::FETCH_ASSOC);

        if ($qr->rowCount() > 0) {
            $error = "<p class=\"error\">Login or email already exists. Please choose a different one.</p>";
        } else {
            // Insert into the users table
			$salt = generateSalt();
			$hashedPassword = hashPasswordWithSalt($password, $salt);
			$pwhash = $salt . '$' . $hashedPassword;
            //$pwhash = hashPassword($password);


			$sql = "INSERT INTO users (login, email, pwhash) VALUES (:login, :email, :pwhash)";
            $qr = $conn->prepare($sql);
            $qr->bindParam(':login', $login, PDO::PARAM_STR);
            $qr->bindParam(':email', $email, PDO::PARAM_STR);
            $qr->bindParam(':pwhash', $pwhash, PDO::PARAM_STR);
            if (!$qr->execute()) {
                throw new Exception('Error inserting user into the database.');
            }
    
            // Get the newly created user ID
            $user_id = $conn->lastInsertId();

            // Insert into the userinfos table
            
			$sql = "INSERT INTO userinfos (userid, birthdate, location, bio, avatar) VALUES (:userid, NULL, '', '', '')";
            $qr = $conn->prepare($sql);
            $qr->bindParam(':userid', $user_id, PDO::PARAM_INT);
              // Check for errors during execution
            if (!$qr->execute()) {
                throw new Exception('Error inserting user info into the database.');
            }

            $error = "<p class=\"success\">Registration successful! You can now <a href='connexion.php'>log in</a>.</p>";
        }
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
			
        form {
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
			.error { color: red; }
      .success { color: green; }
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
								<h2>Sign Up</h2>
						
						 <?php if (isset($error)): ?>
					      <?php echo $error; ?>
					  <?php endif; ?>

					  <form method="POST" action="signup.php" id="signup-form">
					  <!-- Login -->
								<label for="login">Login:</label>
								<input type="text" id="login" name="login" required>

								<!-- Email -->
								<label for="email">Email:</label>
								<input type="email" id="email" name="email" required>

								<!-- Password -->
								<label for="password">Password:</label>
								<input type="password" id="password" name="password" required>

								<!-- Confirm Password -->
								<label for="password_confirm">Confirm Password:</label>
								<input type="password" id="password_confirm" name="password_confirm" required>

								<!-- Submit Button -->
								<button type="submit" class="w3-button w3-theme w3-margin">Sign Up</button>
						</form>
					</div>
					</div>
					</div>
					</div>
					</div>
</body>
<!-- Client-Side Validation Script -->
<script>
        document.getElementById("signup-form").addEventListener("submit", function(e) {
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("password_confirm").value;

            const errors = [];

            // Check password length
            if (password.length < 8) {
                errors.push("Password must be at least 8 characters long.");
            }
            // Check for uppercase letters
            if (!/[A-Z]/.test(password)) {
                errors.push("Password must include at least one uppercase letter.");
            }
            // Check for lowercase letters
            if (!/[a-z]/.test(password)) {
                errors.push("Password must include at least one lowercase letter.");
            }
            // Check for a number
            if (!/\d/.test(password)) {
                errors.push("Password must include at least one number.");
            }
            // Check for a special character
            if (!/[\W_]/.test(password)) {
                errors.push("Password must include at least one special character.");
            }
            // Confirm password matches
            if (password !== confirmPassword) {
                errors.push("Passwords do not match.");
            }
            if (errors.length > 0) {
                e.preventDefault(); // Prevent form submission
                alert(errors.join("\n")); // Display errors
            }
        });
    </script>
</html>

