import warp_lane_server.managers.user_manager as user_man
import warp_lane_server.exceptions as wl_exceptions
import warp_lane_server.text as wl_text

from sanic import Sanic, response
from sanic.response import json
from sanic.log import logger


server_home_dir = "/tmp"
app = Sanic(__name__)
app.config.PORT = 8001


@app.route("/", methods=["GET", "OPTIONS"])
def main(request):
    """
    Placeholder main page. Just returns some text.
    """
    return response.text("I'm the warp-lane-server.", status=200)


@app.post("/login")
def main(request):
    """
    Handle HTTP requests to login to the server.

    If correct username and password, returns a session ID that is needed
    for all other endpoints.

    If username or password are wrong, status 400 response with reason
    in "error" json field.
    """

    # Ensure the request matches specification.
    try:
        username = request.form[wl_text.login_param_username][0]
        given_password = request.form[wl_text.login_param_password][0]
    # Catch malformed requests.
    except (KeyError, IndexError):
        return json(
            {wl_text.generic_error_key: wl_text.generic_message_malformed},
            status=400,
        )

    # Get the user info, check they exist.
    try:
        user = user_man.get_user_from_table(username)
    except wl_exceptions.UserNotFoundError:
        return json(
            {wl_text.generic_error_key: wl_text.login_message_bad_username},
            status=400,
        )

    # Check their supplied credentials.
    try:
        user_man.check_credentials(user, given_password)
    except wl_exceptions.WrongPasswordError:
        return json(
            {wl_text.generic_error_key: wl_text.login_message_bad_pw},
            status=400,
        )

    session_id = user_man.return_valid_session_id_for_user(user)
    return json(
        {wl_text.login_key_session_id: session_id},
        status=200
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)