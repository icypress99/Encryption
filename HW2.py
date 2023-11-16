from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def int_to_bytes(key, length):
    key_bytes = key.to_bytes((length + 7) // 8, byteorder='big')
    return key_bytes

def encrypt_message(message, key):
    iv = b'\x00' * 16

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=None)

    # Create an encryptor using the cipher
    encryptor = cipher.encryptor()

    # Apply padding to the message
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    # Encrypt the padded message
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data

def decrypt_message(encrypted_data, key):
    # Generate a random initialization vector (IV)
    iv = b'\x00' * 16

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=None)

    # Create a decryptor using the cipher
    decryptor = cipher.decryptor()

    # Decrypt the encrypted data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding from the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data



def prime_checker(num):
    if num < 1:
        return -1
    elif num > 1:
        if num == 2:
            return 1
        for i in range(2, num):
            if num % i == 0:
                return -1
            return 1

while 1:
    p = int(input("p = "))
    if prime_checker(p) == 1:
        break
    else:
        print("Enter prime number ")

while 1:
    g = int(input("g = "))
    if prime_checker(g) == 1:
        break
    else:
        print("Enter prime number ")

a = int(input("Abbas's Private key = "))
b = int(input("Amir's Private key = "))
message = input("Message = ")

a_public_key = p**a % g
b_public_key = p**b % g

shared_key = a_public_key ** b % g
shared_key_2 = a_public_key ** b % g

print(shared_key)
print(shared_key_2)

# Encrypt the message using the shared key
encrypted_message = encrypt_message(message, int_to_bytes(shared_key,256))

# Decrypt the encrypted message using the shared key
decrypted_message = decrypt_message(encrypted_message, int_to_bytes(shared_key,256))

# Print the results
print(f"Encrypted Message: {encrypted_message.hex()}")
print(f"Decrypted Message: {decrypted_message.decode()}")
print(f"Plain Text: {message}")





