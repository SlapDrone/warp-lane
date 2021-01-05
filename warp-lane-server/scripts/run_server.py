import warp_lane_server.managers.user_manager as user_man
import warp_lane_server.exceptions as wl_exceptions


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
        username = request.form["username"][0]
        given_password = request.form["password"][0]
    except (KeyError, IndexError):
        return json(
            {"error": "Malformed request parameters"},
            status=400,
        )

    # Get the user info, check they exist.
    try:
        user = user_man.get_user_from_table(username)
    except wl_exceptions.UserNotFoundError:
        return json(
            {"error": "User not found"},
            status=400,
        )

    # Check their supplied credentials.
    try:
        user_man.check_credentials(user, given_password)
    except wl_exceptions.WrongPasswordError:
        return json(
            {"error": "Incorrect password"},
            status=400,
        )

    session_id = user_man.return_valid_session_id_for_user(user)
    return json(
        {"session_id": session_id},
        status=200
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)