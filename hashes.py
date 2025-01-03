import hashlib

#8695
#5678uiop
#malachi

# Function to hash a password and compare with a given hash
def check_password_hash(password, hash_value, algorithm='sha1'):
    # Hash the password with the specified algorithm
    if algorithm == 'sha1':
        hashed_password = hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'md5':
        hashed_password = hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    else:
        print(f"Algorithm {algorithm} is not supported.")
        return False
    
    # Compare the hashed password with the provided hash value
    if hashed_password == hash_value:
        print(f"{password} matches the {algorithm.upper()} hash!")
        return True
   
# Example usage:
algorithm = "sha256"
hash_value = "b81848b9e4857c5ed8da601fa6ba92d9c2ee6c6aceabcf5e09813b427dab7bfc"

file_path = "./10k-worst-passwords.txt"

with open(file_path, 'r') as file:
            # Read each line and strip any leading/trailing whitespace
            values = [line.strip() for line in file]

for value in values:
    password = value
    check_password_hash(password, hash_value, algorithm)
     


# Call the function to check if the password matches the hash