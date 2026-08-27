import hashlib

password = "Game@123"

sha256_hash = hashlib.sha256(password.encode()).hexdigest()

print("Original Password:", password)
print("SHA-256 Hash:", sha256_hash)

import bcrypt

password_bytes = password.encode()
bcrypt_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print("bcrypt Hash:", bcrypt_hash.decode())

# Controlled Offline Dictionary Attack

candidate_passwords = [
    "123456",
    "password",
    "Game@123",
    "admin123",
    "welcome123"
]

target_hash = bcrypt_hash

print("\nControlled Offline Attack:")
for candidate in candidate_passwords:
    if bcrypt.checkpw(candidate.encode(), target_hash):
        print("Password Found:", candidate)
        break
else:
    print("Password Not Found")


# Password Reuse Analysis

users = {
    "User1": "Game@123",
    "User2": "Game@123",
    "User3": "Welcome@123",
    "User4": "Welcome@123",
    "User5": "Secure#456"
}

print("\nPassword Reuse Analysis:")
for user, pwd in users.items():
    print(user, ":", pwd)


from collections import Counter

password_counts = Counter(users.values())

print("\nReuse Results:")
for password, count in password_counts.items():
    if count > 1:
        print(password, "used by", count, "users")
    else:
        print(password, "used by", count, "user - Unique")


# After Mitigation Test

strong_password = "G@m3Secure#789!"

strong_hash = bcrypt.hashpw(
    strong_password.encode(),
    bcrypt.gensalt()
)

print("\nAfter Mitigation Test:")

found = False
for candidate in candidate_passwords:
    if bcrypt.checkpw(candidate.encode(), strong_hash):
        print("Password Found:", candidate)
        found = True
        break

if not found:
    print("Password Not Found")


# Verification
correct_password = "Game@123"
wrong_password = "Wrong@123"

print("\nVerification:")
print("Correct Password:", bcrypt.checkpw(correct_password.encode(), bcrypt_hash))
print("Wrong Password:", bcrypt.checkpw(wrong_password.encode(), bcrypt_hash))



