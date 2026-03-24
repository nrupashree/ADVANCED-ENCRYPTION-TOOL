import os
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import constant_time
import base64

# Generate AES-256 key from password
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256-bit key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Encrypt file
def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)

    with open(file_path, 'rb') as f:
        data = f.read()

    # Padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # AES Encryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    output_file = file_path + ".enc"
    with open(output_file, 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f"✅ File encrypted successfully: {output_file}")

# Decrypt file
def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = data[:16]
    iv = data[16:32]
    encrypted_data = data[32:]

    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

    output_file = file_path.replace(".enc", "_decrypted")
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print(f"✅ File decrypted successfully: {output_file}")

# Menu-driven UI
def main():
    while True:
        print("\n🔐 Advanced Encryption Tool (AES-256)")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            file_path = input("Enter file path: ")
            password = input("Enter password: ")
            encrypt_file(file_path, password)

        elif choice == '2':
            file_path = input("Enter encrypted file path: ")
            password = input("Enter password: ")
            decrypt_file(file_path, password)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
