from warp_lane_server.dal.dal import DAL
from warp_lane_server.managers.session_manager import create_session, get_sessionid_for_userid, delete_session
from warp_lane_server.utils.password_encryptor import encrypt_password, check_password

dal = DAL()


def login(username, unencrypted_password):
    sessionid = None
    sql_query = (
        'SELECT userid, password FROM USERS WHERE username=%s;'
    )
    sql_result = dal.run_sql(sql_query, [username])
    userid, encrypted_password = sql_result[0]
    valid = check_password(unencrypted_password, encrypted_password.encode("utf8"))

    if valid:
        sessionid = get_sessionid_for_userid(userid)
        if not sessionid:
            sessionid = create_session(userid)
    return sessionid


def create_user(username, unencrypted_password, email_address):
    """
    Parameters
    ==========

    username: string
    unencrypted_password: string
    email_address: string
    """
    sql_query = (
        'INSERT INTO users (username, password, emailaddress) VALUES (%s, %s, %s)'
    )
    sql_result = dal.run_sql(sql_query,[username, unencrypted_password, email_address])


def delete_user(username):
    """
    Parameters
    ==========

    username: string
    """
    sql_query = (
        'DELETE FROM users WHERE username = %s'
    )
    sql_result = dal.run_sql(sql_query,[username])


def get_user(username):
    """
    Parameters
    ==========

    username: string
    """
    sql_query = (
        'SELECT * FROM users WHERE username = %s'
    )
    sql_result = dal.run_sql(sql_query,[username])
    return sql_result[0]


def logout(sessionid):
    """
    Parameters
    ==========
    sessionid: string
    """
    delete_session(sessionid)
