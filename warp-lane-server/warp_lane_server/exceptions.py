"""
Module for custom exceptions in warp_lane_server
"""


class WLException(Exception):
    """Base exception type for warp-lane"""


################################################################################
# Exceptions raised when querying the user table.
################################################################################
class UserNotFoundError(WLException):
    def __init__(self, username):
        self.username = username
        self.message = f'User: {username} not found in user table.'
        super().__init__(self.message)


class WrongPasswordError(WLException):
    def __init__(self):
        super().__init__('Wrong password')


class UserBuildError(WLException):
    def __init__(self):
        super().__init__()