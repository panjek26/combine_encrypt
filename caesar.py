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

def encrypt_data(data, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a cipher object with AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    # Pad the data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    # Encrypt the data using the cipher object
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Combine the IV and encrypted data
    combined_data = iv + encrypted_data

    # Return the encrypted data as a base64-encoded string
    return combined_data.hex()

def main():
    generate_key()
    key = load_key()
    data = "This is a secret message."
    encrypted_data = encrypt_data(data, key)
    print(f"Encrypted data: {encrypted_data}")

if __name__ == '__main__':
    main()

# Streamlit app
st.title("AES Encryption")

st.header("Encrypt some data")

data = st.text_input("Enter some data to encrypt")

if st.button("Encrypt"):
    key = load_key()
    encrypted_data = encrypt_data(data, key)
    st.write(f"Encrypted data: {encrypted_data}")
