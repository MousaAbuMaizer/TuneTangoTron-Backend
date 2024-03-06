import bcrypt

class EncryptService:

    def getHashedPassword(password):
        # Generate a salt and hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Ensure the hashed password is stored as a string (UTF-8)
        return hashed_password.decode('utf-8')

    def checkPassword(input_password, stored_hashed_password):
        # Ensure stored_hashed_password is decoded from string to bytes
        stored_hashed_password_bytes = stored_hashed_password.encode('utf-8')
        # Check if the input password matches the stored hashed password
        return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password_bytes)
