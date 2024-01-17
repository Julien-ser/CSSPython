from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    print("Key: ", key.decode())
    return key

def encrypt(plain_text, key):
    plain_text = plain_text.encode()
    cipher_text = Fernet(key).encrypt(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(cipher_text, key):
    cipher_text = cipher_text.encode()
    plain_text = Fernet(key).decrypt(cipher_text)
    plain_text = plain_text.decode()
    return plain_text

encKey = ""

while True:
    method = input("(c/e/d)")
    if method == "c":
        encKey = create_key()
    elif method == "e":
        text = input(">>")
        cipher_text = encrypt(text, encKey)
        print(cipher_text)
    elif method == "d":
        text = input(">>")
        cipher_text = decrypt(text, encKey)
        print(cipher_text)
        
