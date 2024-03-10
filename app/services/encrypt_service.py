import hashlib

def encrypt_password(password):

    password_bytes = password.encode('utf-8')
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(password_bytes)
    encrypted_password = hash_algorithm.hexdigest()

    return encrypted_password