import hashlib
import hmac

# Given keys
key_1 = b"1234"
key_2 = b"5678"

# Given messages and HMACs
messages = [
    ("Challenge 2.2 is easy.", "12d44a1c2448cc54ddffc75e69313a7964d5d775"),
    ("Challenge 2.2 is doable.", "1b25d0e281f73935f7a122c088c1bc34686b271b"),
    ("Challenge 2.2 is hard.", "aec64e480f251c6811686597305b04edcc25da35")
]

# Function to calculate HMAC
def calculate_hmac(key_1, key_2, msg):
    inner_hmac = hmac.new(key_1, msg.encode(), hashlib.sha1).digest()
    final_hmac = hmac.new(key_2, inner_hmac, hashlib.sha1).hexdigest()
    return final_hmac

# Verify each message's HMAC
results = []
for msg, given_hmac in messages:
    computed_hmac = calculate_hmac(key_1, key_2, msg)
    results.append((msg, computed_hmac, computed_hmac == given_hmac))

results