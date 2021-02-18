import warp_lane_server.managers.session_manager as sesh_man
import warp_lane_server.utils.password_encryptor as pw_enc
import warp_lane_server.exceptions as wl_exceptions
from warp_lane_server.dal.dal import DAL


dal = DAL()


class User:
    """
    Simple class to encapsulate user info.
    """
    def __init__(self):
        self.user_id = None
        self.username = None
        # self.pw = None
        self.encrypted_pw = None
        self.email = None
        self.date_added = None
        self.date_last_seen = None

    @classmethod
    def from_sql(cls, sql):
        """
        Build the user interface from a row in the user table

        Parameters
        ----------
        sql: tuple - values for row.

        Returns
        -------
        User - instance of User class

        Raises
        ------
        warp_lane_server.exceptions.UserBuildError
        """
        try:
            user = cls()
            user.user_id = sql[0]
            user.username = sql[1]
            user.encrypted_pw = sql[2]
            user.email = sql[3]
            user.date_added = sql[4]
            user.date_last_seen = sql[5]
            return user
        except (IndexError, TypeError):
            raise wl_exceptions.UserBuildError


def get_user_from_table(username):
    """
    Get the row of data from the user table for this username.

    Parameters
    ----------
    username: string

    Returns
    -------
    Instance of User class with data populated from SQL users table

    Raises
    ------
    warp_lane_server.exceptions.UserNotFoundError if user not found.
    """
    try:
        sql_query = (
            'SELECT * FROM users WHERE username = %s'
        )
        sql_result = dal.run_sql(sql_query, (username,))
        return User.from_sql(sql_result[0])
    except IndexError:
        raise wl_exceptions.UserNotFoundError(username)


def check_credentials(user, unencrypted_password):
    """
    Cross check the user's id and credentials with the user database.

    Parameters
    ----------
    user: User
    unencrypted_password: str

    Raises
    ------
    warp_lane_server.exceptions.WrongPassWordError if wrong pw.

    """
    valid = pw_enc.check_password(
        unencrypted_password,
        user.encrypted_pw.encode("utf8")
    )
    if not valid:
        raise wl_exceptions.WrongPasswordError


def return_valid_session_id_for_user(user):
    """
    Use the session manager layer to return a valid session ID, creating
    a new one if necessary.

    Parameters
    ----------
    user: User

    Returns
    -------
    session_id: str
    """
    session_id = sesh_man.get_session_id_for_user_id(user.user_id)
    if not session_id:
        session_id = sesh_man.create_session(user.user_id)
    return session_id


def login_backend(username, given_password):
    """Backend function to carry out the full login process."""
    user = get_user_from_table(username)
    check_credentials(user, given_password)
    return return_valid_session_id_for_user(user)


def create_user(username, unencrypted_password, email_address):
    """
    Parameters
    ----------

    username: string
    unencrypted_password: string
    email_address: string
    """
    sql_query = (
        'INSERT INTO users (username, password, emailaddress) VALUES (%s, %s, %s)'
    )
    sql_result = dal.run_sql(
        sql_query,
        (username, unencrypted_password, email_address)
    )


def delete_user(username):
    """
    Parameters
    ----------

    username: string
    """
    sql_query = (
        'DELETE FROM users WHERE username = %s'
    )
    sql_result = dal.run_sql(sql_query, (username,))


def logout(session_id):
    """
    Parameters
    ----------
    session_id: string
    """
    sesh_man.delete_session(session_id)
