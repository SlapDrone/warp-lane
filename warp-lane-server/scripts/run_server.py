import warp_lane_server.managers.user_manager as user_man
import warp_lane_server.exceptions as wl_exceptions
import warp_lane_server.text as wl_text

from sanic import Sanic, response
from sanic.response import json
from sanic.log import logger
from sanic_cors import CORS, cross_origin
from json import loads as json_loads

server_home_dir = "/tmp"
app = Sanic(__name__)
app.config.PORT = 8001
CORS(app)


@app.route("/", methods=["GET", "OPTIONS"])
def main(request):
    """
    Placeholder main page. Just returns some text.
    """
    return response.text("I'm the warp-lane server.", status=200)


@app.post("/login")
def login(request):
    """
    Handle HTTP requests to login to the server.

    If correct username and password, returns a session ID that is needed
    for all other endpoints.

    If username or password are wrong, status 400 response with reason
    in "error" json field.
    """
    # Ensure the request matches specification.
    try:
        # SM: hackily modified this for the sake of the webapp feel free to refactor!
        if request.body:
            body = json_loads(request.body)
            username = body[wl_text.login_param_username]
            given_password = body[wl_text.login_param_password]
        else:
            username = request.form[wl_text.login_param_username][0]
            given_password = request.form[wl_text.login_param_password][0]
    except (KeyError, IndexError):
        return json(
            {wl_text.generic_error_key: wl_text.generic_message_malformed},
            status=400,
        )

    # Use the backend to get a session ID.
    try:
        session_id = user_man.login_backend(username, given_password)
        return json(
            {wl_text.session_id_key: session_id},
            status=200
        )
    # Handle bad usernames or passwords.
    except wl_exceptions.UserNotFoundError:
        return json(
            {wl_text.generic_error_key: wl_text.login_message_bad_username},
            status=400,
        )
    except wl_exceptions.WrongPasswordError:
        return json(
            {wl_text.generic_error_key: wl_text.login_message_bad_pw},
            status=400,
        )


@app.get("/get_unmodified_tracks")
def get_unmodified_tracks(request):
    """
    Get the unmodified tracks for this user.

    Requires the parameter session_id.
    """
    # Ensure the request matches specification.
    try:
        session_id = request.args[wl_text.session_id_key][0]
    # Catch malformed requests.
    except (KeyError, IndexError):
        return json(
            {wl_text.generic_error_key: wl_text.generic_message_malformed},
            status=400,
        )

    return response.text("Placeholder success text.", status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)