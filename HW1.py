import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes


def readFile(path):
    with open(path, 'rb') as file:
        data = file.read()
    return data

encoded_message = 'RsdnPS51icNeUoRT6X4y5ex3uHr4GBl9ynCx2+aTAxRm/0q47HO/+4QXm3AlQqEy8ZWMYvQ+65qzf2TwYLAFN/g+FJPFIByfBtcKLale85uMVJXKn8pRsUrvAFxAUsj8G81gXvKVZDHgy8lU0piec5vH6RXQlEPakXPWyPCft414fUnCzJdhG+S20WwLODBiEz7ov9XsP/BEb7y02VC3CYuMHaPrHiSRKmB8zFM2OigpKXpHauZy/ANq9KPu68pJb+YDfAuExtjmIDrnOl7cTw0itd8HXUYzuKiRClBEJ/jDYRaJRizq5SO4yzkXsPOd/IzHMcAS7/CH/O57lZ56Pw=='

if __name__ == '__main__':
    data = readFile('private_key.pem')
    private_key = serialization.load_pem_private_key(data, password=None)

    data = readFile('public_key.pem')
    public_key = serialization.load_pem_public_key(data, backend=None)

    decoded_bytes = base64.b64decode(encoded_message.encode('utf-8'))
    decrypted_message = private_key.decrypt(
        decoded_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(f"Decrypted message: {decrypted_message.decode('utf-8')}")


