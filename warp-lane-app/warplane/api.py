""" api.py

    An API class for talking to the central server
"""

endpoints = ["login"]

# 'login?username=steve&password=balabalba'


class API:
    def __init__(
        self, server_url: str = "https://blah.example.com", port: int = 6666
    ):
        pass

    def login(self, username: str, password: str):
        # the server will supply a session id upon successful login
        # store session id as this will be used with all subsequent requests
        self.session_id = ...
        pass

    def send_interface_metadata(self):
        # REQUIRES SESSION ID
        pass

    def send_connected_device_metadata(self):
        # REQUIRES SESSION ID
        pass

    def get_track_list(self):
        # REQUIRES SESSION ID
        # pass username, sessionid
        pass

    def download_original_tracks(self):
        # REQUIRES SESSION ID
        pass

    def upload_modified_tracks(self):
        # REQUIRES SESSION ID
        pass
