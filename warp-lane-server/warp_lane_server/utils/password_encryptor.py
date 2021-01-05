import bcrypt


def encrypt_password(unencrypted_password):
    return bcrypt.hashpw(unencrypted_password.encode(), bcrypt.gensalt())


def check_password(unencrypted_password, hash_and_salt):
    """
    Parameters
    ==========

    unencrypted_password: string
        This is the plain text password input by the user.
    hash_and_salt: bytes
        This is stored in the database it should be utf8
        encoded e.g. hash_and_salt.encode('utf8')

    Returns
    =======
    valid: boolean
        True if passwords match else false.
    """
    return bcrypt.checkpw(unencrypted_password.encode(), hash_and_salt)


if __name__ == "__main__":
    encrypted_password = encrypt_password("secret")
    print(encrypted_password)
    # noinspection SpellCheckingInspection
    my_hash_and_salt = "$2b$12$Yc2qjXGtOsFqR6ck6v2ruOCIM6FRjIpsnf5zL54H/CPnmt7KhldHO"
    valid = check_password("secret", my_hash_and_salt.encode("utf8"))
    print(valid)
