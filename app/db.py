from flask_bcrypt import Bcrypt
import getpass

bcrypt = Bcrypt()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")

def prompt_password():
    pw1 = getpass.getpass("Enter password: ")
    pw2 = getpass.getpass("Confirm password: ")
    if pw1 != pw2:
        raise ValueError("Passwords do not match.")
    return pw1
