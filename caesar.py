from flask import Flask, render_template, request
import streamlit as st

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        encrypted_text = caesar_cipher(text, shift)
        return render_template('caesar.html', encrypted_text=encrypted_text)
    return render_template('caesar.html')

@app.route('/substitution', methods=['GET', 'POST'])
def substitution():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        encrypted_text = substitution_cipher(text, key)
        return render_template('substitution.html', encrypted_text=encrypted_text)
    return render_template('substitution.html')

if __name__ == '__main__':
    app.run(debug=True)
