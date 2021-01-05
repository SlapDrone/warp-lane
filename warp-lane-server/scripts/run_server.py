import warp_lane_server.managers.user_manager as user_man

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
    return response.text("I'm a teapot", status=200)


@app.post("/login")
def main(request):
    """
    Handle HTTP requests to login to the server.

    If correct username and password, returns a session ID that is needed
    for all other endpoints.

    If username or password are wrong, status 400 response with reason
    in "error" json field.
    """

    try:
        username = request.form["username"][0]
        password = request.form["password"][0]
        session_id = user_man.login(username, password)

        if session_id == 'no_user':
            logger.info(session_id)
            logger.info('User not found')
            return json(
                {"error": "user not recognised"},
                status=400,
            )
        if session_id == 'wrong_password':
            logger.info(session_id)
            logger.info('wrong password')
            return json(
                {"error": "incorrect password"},
                status=400,
            )

        return json(
            {"session_id": session_id},
            status=200
        )

    except KeyError:
        return json(
            {"error": "malformed parameters"},
            status=400,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)