import base64

def encode_data(plain_text):
    plain_text = plain_text.encode()
    cipher_text = base64.b64encode(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text

def decode_data(cipher_text):
    plain_text = base64.b64decode(cipher_text)
    plain_text = plain_text.decode()
    return plain_text

while True:
    method = input("(e/d)").lower()
    message = input(">>")

    if method == "e":
        print(encode_data(message))
    else:
        print(decode_data(message))
