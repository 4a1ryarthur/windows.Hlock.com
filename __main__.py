file_to_encrypt = "C:/"
    encryption_key = generate_key()

    # Encrypt the file
    encrypt_file(file_to_encrypt, encryption_key)

    # Decrypt the file
    decrypt_file(file_to_encrypt + ".enc", encryption_key)
