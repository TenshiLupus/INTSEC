def caesar_decrypt_extended(ciphertext, key):
    # Define the 37-character search space
    search_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
    plaintext = ""
    for char in ciphertext:
        if char in search_space:
            idx = search_space.index(char)
            new_idx = (idx + 1 - key) % 37
            plaintext += search_space[new_idx]
        else:
            plaintext += char  # Keep non-search space characters unchanged
    return plaintext

def brute_force_caesar_extended(ciphertext):
    # Try all possible keys in the 37-character search space
    search_space_size = 37
    print("Brute Force Results:")
    for key in range(1,search_space_size + 1):
        decrypted_text = caesar_decrypt_extended(ciphertext, key)
        print(f"Key {key}: {decrypted_text}")

# Example ciphertext
ciphertext = "D_AZ_5H7S006_9WHF6BHD_33HX_5VHSAH3WS0AHIJHX3SY0H064WH6XHAZW4HS9WHX_3WH5S4WVHX3SYH5HTBAH064WA_4W0HAZWHX3SYH_0HZ_VVW5H_5HS56AZW9HX_3WHAZ_0H4W00SYWH_0HAZWHS50DW9HA6HUZS33W5YWHIHV6AHI"

# Run brute force decryption
brute_force_caesar_extended(ciphertext)


def caesar_decrypt_extended(ciphertext, key):
    # Define the 37-character search space
    search_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
    plaintext = ""
    for char in ciphertext:
        if char in search_space:
            # Find the position in the search space and shift backward
            idx = search_space.index(char)
            new_idx = (idx - key) % 37
            plaintext += search_space[new_idx]
        else:
            # Keep non-search space characters unchanged
            plaintext += char
    return plaintext


# # Decrypt the ciphertext
# plaintext = caesar_decrypt_extended(ciphertext, 1)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 2)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 3)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 4)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 5)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 6)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 7)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 8)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 9)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 10)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 11)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 12)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 13)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 14)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 15)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 16)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 17)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 18)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 19)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 20)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 21)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 22)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 23)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 24)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 25)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 26)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 27)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 28)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 29)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 30)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 31)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 32)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 33)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 34)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 35)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 36)
# print("Decrypted Text:", plaintext)
# plaintext = caesar_decrypt_extended(ciphertext, 37)
# print("Decrypted Text:", plaintext)

def decrypt_to_plaintext(ciphertext, target_plaintext):
    # Define the 37-character search space
    search_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
    # Find the shift (key) using the first pair of matching characters
    key = (search_space.index(ciphertext[0]) - search_space.index(target_plaintext[0])) % 37
    # Decrypt the ciphertext with the identified key
    decrypted_text = caesar_decrypt_extended(ciphertext, key)
    return decrypted_text, key

# Ciphertext and expected plaintext
ciphertext = "VHQG34CVHN3WR3FDUODOLFH"
target_plaintext = "SEND_10SEK_TO_CARLALICE"
decrypted_text, key = decrypt_to_plaintext(ciphertext, target_plaintext)
    