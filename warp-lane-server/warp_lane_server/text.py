"""
Basic module for holding text vars that are used in multiple places,
e.g. the server and the pytests for the server.
"""

# Generic response messages/keys
generic_message_malformed = 'Malformed request parameters.'
generic_error_key = "error"

# Session messages/keys
session_id_key = 'session_id'

# Login response messages/keys
login_param_username = 'username'
login_param_password = 'password'
login_param_email_address = 'email_address'

login_message_bad_pw = 'Wrong password.'
login_message_bad_username = 'User not found.'

create_user_error = "An error occurred creating the user."