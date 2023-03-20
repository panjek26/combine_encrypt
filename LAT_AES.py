import streamlit as st
from Crypto.Cipher import AES
import os

def generate_key():
    key = os.urandom(32)
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def pad(data):
    length = AES.block_size - (len(data) % AES.block_size)
    return data + (chr(length) * length).encode()

def encrypt_data(data, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a cipher object with AES algorithm and CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the data
    padded_data = pad(data)

    # Encrypt the data using the cipher object
    encrypted_data = cipher.encrypt(padded_data)

    # Combine the IV and encrypted data
    combined_data = iv + encrypted_data

    # Return the encrypted data as a base64-encoded string
    return combined_data.hex()

def main():
    generate_key()
    key = load_key()
    data = "This is a secret message."
    encrypted_data = encrypt_data(data.encode(), key)
    print(f"Encrypted data: {encrypted_data}")

if __name__ == '__main__':
    main()

# Streamlit app
st.title("AES Encryption")

st.header("Encrypt some data")

data = st.text_input("Enter some data to encrypt")

if st.button("Encrypt"):
    key = load_key()
    encrypted_data = encrypt_data(data.encode(), key)
    st.write(f"Encrypted data: {encrypted_data}")
