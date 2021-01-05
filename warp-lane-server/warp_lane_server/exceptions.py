"""
Module for custom exceptions in warp_lane_server.
"""


class WLException(Exception):
    """Base exception type for warp-lane"""


################################################################################
# Exceptions raised when querying the session table.
################################################################################
class SessionBuildError(WLException):
    """
    Raised when a Session instance fails to build itself from the sessions
    table.
    """
    def __init__(self, input_data):
        self.message = f'Session build error: {input_data}'
        super().__init__(self.message)


class SessionNotFoundError(WLException):
    """Raised when a session id does not exist in the session table."""
    def __init__(self, session_id):
        self.session_id = session_id
        self.message = f'Session ID does not exist: {session_id}'
        super().__init__(self.message)


################################################################################
# Exceptions raised when querying the user table.
################################################################################
class UserNotFoundError(WLException):
    """Raised when a username does not exist in the user table."""
    def __init__(self, username):
        self.username = username
        self.message = f'User: {username} not found in user table.'
        super().__init__(self.message)


class WrongPasswordError(WLException):
    """Raised when the given password is incorrect."""
    def __init__(self):
        super().__init__('Wrong password')


class UserBuildError(WLException):
    """Raised when a User instance fails to build itself from sql data."""
    def __init__(self, input_data):
        self.message = f'User build error: {input_data}'
        super().__init__(self.message)
