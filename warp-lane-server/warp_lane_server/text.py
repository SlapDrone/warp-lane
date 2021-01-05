"""
Basic module for holding text vars that are used in multiple places,
e.g. the server and the pytests for the server.
"""

# Generic response messages/keys
generic_message_malformed = 'Malformed request parameters.'
generic_error_key = "error"

# Login response messages/keys
login_param_username = 'username'
login_param_password = 'password'

login_message_bad_pw = 'Wrong password.'
login_message_bad_username = 'User not found.'

login_key_session_id = 'session_id'
