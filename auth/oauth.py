from argon2 import PasswordHasher, exceptions


ph = PasswordHasher()


def password_hasher(password: str):
    return ph.hash(password)


def verify_hash(hash_password: str, password: str) -> bool:
    val = False
    try:
        val = ph.verify(hash_password, password)
        return val
    except exceptions.VerificationError:
        print("Validation Error: Wrong Password")
    except:
        print("Error Occurred During Validation")
    return val
