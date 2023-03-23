import streamlit as st

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def substitution_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += key[ord(char) - 65].upper()
            else:
                result += key[ord(char) - 97]
        else:
            result += char
    return result


def dec_caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def dec_substitution_cipher(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            index = key.find(char)
            result += chr(index + 65)
        else:
            index = key.find(char)
            result += chr(index + 97)
    return result.lower()

def combine_cipher(text, shift, key):
    text = caesar_cipher(text, shift)
    text = substitution_cipher(text, key)
    return text

def decrypt_combine_cipher(text, shift, key):
    text = dec_substitution_cipher(text, key)
    text = dec_caesar_cipher(text, shift)
    return text

def main():
    st.title("Cipher")
    option = st.sidebar.selectbox("Select the Cipher", ["Encrypt Combine Cipher", "Decrypt Combine Cipher"])

    if option == "Encrypt Combine Cipher":
        st.subheader("Encrypt using Combine Cipher")
        text = st.text_input("Enter the text to be encrypted", "")
        shift = st.number_input("Enter the shift value", value=0, step=1, min_value=0, max_value=25)
        key = st.text_input("Enter the key (26 alphabets only)", "qwertyuiopasdfghjklzxcvbnm",type="password")
        if st.button("Encrypt"):
            if len(key) != 26:
                st.error("Key should have 26 alphabets only")
            else:
                encrypted_text = combine_cipher(text, shift, key)
                st.success("Encrypted Text: {}".format(encrypted_text))
    elif option == "Decrypt Combine Cipher":
        st.subheader("Decrypt using Combine Cipher")
        text = st.text_input("Enter the text to be decrypted", "")
        shift = st.number_input("Enter the shift value", value=0, step=1, min_value=0, max_value=25)
        key = st.text_input("Enter the key (26 alphabets only)", "qwertyuiopasdfghjklzxcvbnm",type="password")
        if st.button("Decrypt"):
            if len(key) != 26:
                st.error("Key should have 26 alphabets only")
            else:
                encrypted_text = decrypt_combine_cipher(text, shift, key)
                st.success("Decrypted Text: {}".format(encrypted_text))


if __name__ == '__main__':
    main()
