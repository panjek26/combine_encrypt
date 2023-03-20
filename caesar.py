import streamlit as st
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a cipher object with AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    # Encrypt the file data using the cipher object
    encryptor = cipher.encryptor()
    padded_data = encryptor.update(pad_data(file_data)) + encryptor.finalize()

    # Write the encrypted data and IV to a new file
    with open(f"{file_path}.enc", "wb") as file:
        file.write(iv + padded_data)

    return f"{file_path}.enc"

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Get the IV from the file data
    iv = file_data[:16]

    # Create a cipher object with AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    # Decrypt the file data using the cipher object
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(file_data[16:]) + decryptor.finalize()

    # Remove padding from decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Write the decrypted data to a new file
    with open(f"{file_path}.dec", "wb") as file:
        file.write(unpadded_data)

    return f"{file_path}.dec"

def pad_data(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def main():
    file_path = "example.txt"
    generate_key()
    key = load_key()
    encrypted_file_path = encrypt_file(file_path, key)
    decrypted_file_path = decrypt_file(encrypted_file_path, key)

if __name__ == '__main__':
    main()

# Streamlit app
st.title("AES Encryption and Decryption")

st.header("Upload a file to encrypt")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Save the file to a temporary location
    with open("temp.txt", "wb") as file:
        file.write(uploaded_file.getvalue())

    # Encrypt the file using AES
    key = load_key()
    encrypted_file_path = encrypt_file("temp.txt", key)

    # Download the encrypted file
    st.download_button("Download encrypted file", data=open(encrypted_file_path, "rb").read(), file_name=encrypted_file_path)

st.header("Upload a file to decrypt")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Save the file to a temporary location
    with open("temp.txt.enc", "wb") as file:
        file.write(uploaded_file.getvalue())

   
