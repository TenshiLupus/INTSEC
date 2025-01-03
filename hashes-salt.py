#3649
#PASsw0RD
#
import hashlib

# Function to hash password with salt and check against the provided hash
def check_salted_hash(password, salt, hash_value, algorithm='sha1'):
    # Concatenate salt and password
    salted_password = salt + password
    
    # Hash the salted password using the specified algorithm
    if algorithm == 'sha1':
        hashed_password = hashlib.sha1(salted_password.encode()).hexdigest()
    elif algorithm == 'md5':
        hashed_password = hashlib.md5(salted_password.encode()).hexdigest()
    elif algorithm == 'sha256':
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    else:
        print(f"Algorithm {algorithm} is not supported.")
        return False
    
    # Compare the generated hash with the given hash value
    if hashed_password == hash_value:
        print(f"{password} matches the {algorithm.upper()} hash!")
        return True
   
# Example hashes, salts, and password hints
hashes = [
    {'hash': '57536215cfe9781d21733fcab27a653e9db92577', 'salt': '1fa6', 'algorithm': 'sha1', 'hint': 'PIN code'},
    {'hash': '8421f0e3432bb339f3671341bc1ec96f6eb283dbf65bb56793065458c20cf945', 'salt': 'cb63', 'algorithm': 'sha256', 'hint': 'L1tera11y a password'},
    {'hash': 'e75a0b86d4f30e2e56a73cbe9d7dbf07', 'salt': 'e098', 'algorithm': 'md5', 'hint': 'You need to know something (obvious) about me.'}
]



salt= 'e098'
hash_value= 'e75a0b86d4f30e2e56a73cbe9d7dbf07'
algorithm= 'md5'

# file_path = "./korelogic-password.txt"

# with open(file_path, 'r') as file:
#             # Read each line and strip any leading/trailing whitespace
#             values = [line.strip() for line in file]


# for value in values: 
password = "middle aged"
# Call the function to check if the password matches the hash
check_salted_hash(password, salt,hash_value, algorithm)
