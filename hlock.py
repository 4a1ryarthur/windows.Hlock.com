# You Must Have All Instaled In Your Ejector (Hlock.eject.sh)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generate random key for AES encryption
def generate_key():
    return os.urandom(32)

# Encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    # AES encryption with CBC mode and PKCS7 padding
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data to be a multiple of the block size (128-bit)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save encrypted data to a new file
    with open(file_path + ".enc", 'wb') as f_enc:
        f_enc.write(iv + encrypted_data)

    print(f"{file_path} encrypted successfully.")

# Decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        iv = f.read(16)  # Extract the IV from the beginning of the file
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding from the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Save decrypted data to a new file
    decrypted_file = file_path.replace('.enc', '.dec')
    with open(decrypted_file, 'wb') as f_dec:
        f_dec.write(unpadded_data)

    print(f"{file_path} decrypted successfully.")
