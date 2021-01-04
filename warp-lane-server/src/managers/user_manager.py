from src.dal.dal import DAL
from src.managers.session_manager import create_session, get_sessionid_for_userid
from src.utils.password_encryptor import encrypt_password, check_password

dal = DAL()


def login(username, unencrypted_password):
    sessionid = None
    sql_query = (
        'SELECT "USERID", "PASSWORD" FROM USERS WHERE "USERNAME"=%s;'
    )
    sql_result = dal.run_sql(sql_query, [username])
    userid, encrypted_password = sql_result[0]
    valid = check_password(unencrypted_password, encrypted_password.encode("utf8"))

    if valid:
        sessionid = get_sessionid_for_userid(userid)
        if not sessionid:
            sessionid = create_session(userid)
    return sessionid


if __name__ == "__main__":
    sessionid = login("admin", "secret")
    print(sessionid)
