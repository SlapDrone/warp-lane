from dal.dal import DAL
from managers.session_manager import create_session, get_sessionid_for_userid
from utils.password_encryptor import encrypt_password, check_password

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
            create_session(userid)
            sessionid = get_sessionid_for_userid(userid)
    return sessionid


if __name__ == "__main__":
    sessionid = login("admin", "secret")
    print(sessionid)
