# def xor_decrypt_with_binary_key(file_path, binary_key):
#     # Convert the binary key to bytes
#     key_bits = int(binary_key, 2)  # Convert binary string to an integer
#     key_length = len(binary_key) // 8
#     key = key_bits.to_bytes(key_length, byteorder="big")
#     print(f"Derived key: {key.decode('ascii')}")

#     # Read the encrypted file in binary mode
#     with open(file_path, "rb") as encrypted_file:
#         encrypted_data = encrypted_file.read()

#     # Decrypt the file using the key (repeated cyclically)
#     decrypted_data = bytes([encrypted_data[i] ^ key[i % len(key)] for i in range(len(encrypted_data))])

#     try:
#         # Decode the decrypted data as ASCII
#         ascii_data = decrypted_data.decode("ascii")
#         print(f"Decrypted ASCII content:\n{ascii_data}")
#     except UnicodeDecodeError:
#         print("Decrypted data contains non-ASCII characters and cannot be fully converted to ASCII.")
#         return

#     # Save the decrypted ASCII content to a file
#     output_file = file_path + ".decrypted_ascii.txt"
#     with open(output_file, "w", encoding="ascii") as ascii_file:
#         ascii_file.write(ascii_data)

#     print(f"ASCII-encoded decrypted file saved as: {output_file}")

# # Usage
# file_path = "./Challenge-1.2.enc"  # Replace with your file path
# binary_key = "01000011011010000110000101101100011011000110010101101110011001110110010100100000001100010010111000110010"
# xor_decrypt_with_binary_key(file_path, binary_key)

# Load the file to examine the encrypted data and derive the XOR key
# Load the file to examine the encrypted data and derive the XOR key
# file_path = "./Challenge-1.2.enc"

# # Read the file in binary mode
# with open(file_path, "rb") as encrypted_file:
#     encrypted_data = encrypted_file.read()

# # Known plaintext to derive the key
# known_plaintext = "Challenge 1.2".encode("ascii")

# # Derive the XOR key from the first part of the encrypted data
# derived_key = bytes([encrypted_data[i] ^ known_plaintext[i] for i in range(len(known_plaintext))])

# # Convert the derived key to its binary representation
# derived_key_bits = ''.join((format(byte, '08b') + " ") for byte in derived_key)
# derived_key_bits
# print("DERIVED KEY IS :", derived_key_bits)

# XOR decryption script














# # Encrypted data (ASCII binary values)
# file_path = "./Challenge-1.2.enc"
# with open(file_path, "rb") as encrypted_file:
#     encrypted_data = encrypted_file.read()

# # Convert binary to decimal
# encrypted_bytes = [int(b, 2) for b in encrypted_data]

# # XOR key (you can modify the key here)
# xor_key = 0b01100100011001110110011001100100001101000011011000110100011100110110010001100110001101010011010001111010

# # Decrypt the data using XOR
# decrypted_bytes = [b ^ xor_key for b in encrypted_bytes]

# # Convert the decrypted bytes back to characters
# decrypted_text = ''.join(chr(b) for b in decrypted_bytes)

# # Output the decrypted text
# print("Decrypted text:", decrypted_text)








# def xor_decrypt_with_key(input_file_path, output_file_path, xor_key):
#     try:
#         # Convert XOR key to a list of its bytes (binary form)
#         xor_key_bytes = [int(bit, 2) for bit in xor_key.split()]
        
#         # Open the input encrypted file in binary mode
#         with open(input_file_path, 'rb') as infile:
#             encrypted_data = infile.read()
        
#         # Prepare to decrypt the data
#         decrypted_data = bytearray()

#         # Decrypt each byte with the repeating XOR key
#         for i, byte in enumerate(encrypted_data):
#             # XOR each byte with the corresponding key byte, using modulo to loop through the key
#             xor_byte = xor_key_bytes[i % len(xor_key_bytes)]  # Loop back to the start of the XOR key
#             decrypted_byte = byte ^ xor_byte  # Apply XOR operation
#             decrypted_data.append(decrypted_byte)

#         # Write the decrypted data to the output file
#         decrypted_data = bytes(decrypted_data).decode('ascii')
#         with open(output_file_path, 'w', encoding='ascii') as outfile:
#             outfile.write(decrypted_data)

#         print(f"Decryption successful. Decrypted file saved to: {output_file_path}")

#     except Exception as e:
#         print(f"Error during decryption: {e}")

# # Example usage:
# input_file = "./Challenge-1.2.enc"  # Input file path (your encrypted file)
# output_file = "decrypted_file.txt"  # Output file path (the file to save decrypted content)
# xor_key = "01100100 01100111 01100110 01100100 00110100 00110110 00110100 01110011 01100100 01100110 00110101 00110100 01111010"  # Example XOR key in binary (you can replace it with your actual binary XOR key)

# xor_decrypt_with_key(input_file, output_file, xor_key)







def xor_decrypt_with_key(input_file_path, output_file_path, xor_key_prefix):
    try:
        # Convert the known XOR key prefix to a list of its bytes (binary form)
        xor_key_bytes = [int(bit, 2) for bit in xor_key_prefix.split()]
        
        # Open the input encrypted file in binary mode
        with open(input_file_path, 'rb') as infile:
            encrypted_data = infile.read()

        # Try all combinations for the last 2 bytes (from 0 to 255)
        for byte1 in range(256):  # Byte 1 can range from 0 to 255
            for byte2 in range(256):  # Byte 2 can range from 0 to 255
                # Construct the full XOR key (the first 13 bytes plus the two brute-forced bytes)
                full_xor_key = xor_key_bytes + [byte1, byte2]


                xor_key_bits = ' '.join(format(byte, '08b') for byte in full_xor_key)
               

                # Decrypt the data using the current full XOR key
                decrypted_data = bytearray()
                for i, byte in enumerate(encrypted_data):
                    xor_byte = full_xor_key[i % len(full_xor_key)]  # Loop through the XOR key
                    decrypted_byte = byte ^ xor_byte  # Apply XOR operation
                    decrypted_data.append(decrypted_byte)

                # Convert the decrypted bytes to a string (ASCII)
                decrypted_string = bytes(decrypted_data).decode('ascii', errors='ignore')

                # Check if the decrypted text contains a valid pattern (adjust based on expected output)
                # For example, you could look for the word "flag" or some other pattern in the output
                if "slightly harder to decrypt" in decrypted_string:  # Replace with a specific pattern to check
                    print(f"XOR key in binary: {xor_key_bits}")
                    print(f"Decrypted text: {decrypted_string}")
                    
                    # Save the decrypted data to the output file
                    with open(output_file_path, 'w', encoding='ascii') as outfile:
                        outfile.write(decrypted_string)
                    return  # Exit the function once we find a match

        print("No matching key found")
    
    except Exception as e:
        print(f"Error during decryption: {e}")

# Example usage:
input_file = "./Challenge-1.2.enc"  # Input file path (your encrypted file)
output_file = "decrypted_file.txt"  # Output file path (the file to save decrypted content)
xor_key_prefix = "01100100 01100111 01100110 01100100 00110100 00110110 00110100 01110011 01100100 01100110 00110101 00110100 01111010"  # Known 13-byte XOR key in binary

xor_decrypt_with_key(input_file, output_file, xor_key_prefix)