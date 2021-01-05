import warp_lane_server.managers.user_manager as user_man

from sanic import Sanic, response
from sanic.response import json

server_home_dir = "/tmp"
app = Sanic(__name__)
app.config.PORT = 8001


@app.route("/", methods=["GET", "OPTIONS"])
def main(request):
    """
    Placeholder main page. Just returns some text.
    """
    return response.text("I'm a teapot", status=200)


@app.route("/login", methods=["POST"])
def main(request):
    """
    Handle HTTP requests to login to the server.

    Returns a session ID, needed for all other endpoints.
    """
    request_args = request.get_args()
    try:
        username = request_args["username"]
        password = request_args["password"]
        session_id = user_man.login(username, password)
        return session_id
    except KeyError:
        return json(
            {"error": "malformed parameters"},
            status=400,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)