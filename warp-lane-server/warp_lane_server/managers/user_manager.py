from warp_lane_server.dal.dal import DAL
from warp_lane_server.managers.session_manager import create_session, get_sessionid_for_userid, delete_session
from warp_lane_server.utils.password_encryptor import encrypt_password, check_password

dal = DAL()


def login(username, unencrypted_password):
    """
    Cross check the user's id and credentials with the user database.

    If correct, return session_id.
    Else return a text code for sanic (clumsy but want to refactor a lot of
    this code).
    """
    session_id = None
    sql_query = (
        'SELECT userid, password FROM USERS WHERE username = %s;'
    )
    print(sql_query)
    print(username)
    sql_result = dal.run_sql(sql_query, [username])
    try:
        userid, encrypted_password = sql_result[0]
        print(unencrypted_password)
        print(type(unencrypted_password))
        valid = check_password(unencrypted_password,
                               encrypted_password.encode("utf8"))
    except IndexError:
        return 'no_user'

    if valid:
        session_id = get_sessionid_for_userid(userid)
        if not session_id:
            session_id = create_session(userid)
        return session_id

    return 'wrong_password'


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
