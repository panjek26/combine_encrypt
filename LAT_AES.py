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

def decrypt_data(data, key):
    # Decode the hexadecimal-encoded input data
    data = bytes.fromhex(data)

    # Split the data into the IV and encrypted data
    iv, encrypted_data = data[:16], data[16:]

    # Create a cipher object with AES algorithm and CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data using the cipher object
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove the padding from the decrypted data
    length = decrypted_data[-1]
    return decrypted_data[:-length].decode()

def main():
    generate_key
