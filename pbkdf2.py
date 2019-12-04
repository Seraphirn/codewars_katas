import hashlib
import binascii
import secrets

salt = secrets.token_hex(64)
passwd = '123'
iterat = 100000
print(salt)
print(
    binascii.hexlify(
        hashlib.pbkdf2_hmac('sha512', passwd.encode(), salt.encode(), iterat)
    ).decode()
)
