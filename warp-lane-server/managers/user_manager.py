from dal.dal import DAL
from managers.session_manager import create_session
from utils.password_encryptor import encrypt_password, check_password

dal = DAL()


def login(username, unencrypted_password):
    sql_query = (
        'SELECT "USERID", "PASSWORD" FROM USERS WHERE "USERNAME"=%s;'
    )
    sql_result = dal.run_sql(sql_query, [username])
    user_id, encrypted_password = sql_result[0]
    valid = check_password(unencrypted_password, encrypted_password.encode("utf8"))

    if valid:
        create_session(user_id)
    return valid


if __name__ == "__main__":
    login("admin", "secret")
