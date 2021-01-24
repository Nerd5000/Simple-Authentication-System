import base64


def encrypt(password):
    password_bytes = password.encode('utf-8')
    base64_bytes = base64.b64encode(password_bytes)
    base64_password = base64_bytes.decode('utf-8')
    return base64_password


def decrypt(enrypted_password):
    base64_bytes = enrypted_password.encode('utf-8')
    password_bytes = base64.b64decode(base64_bytes)
    password = password_bytes.decode('utf-8')
    return password
