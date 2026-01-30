from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hash_password(password: str):
    return password_hash.hash(password)


def verify_password(plainpassword,hashed_passwod):
    return password_hash.verify(plainpassword,hashed_passwod)