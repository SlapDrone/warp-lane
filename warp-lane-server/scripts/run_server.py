import warp_lane_server.managers.user_manager

from sanic import Sanic, response


server_home_dir = '/tmp'
app = Sanic(__name__)
app.config.PORT = 8001


@app.route("/", methods=["GET", "OPTIONS"])
def main(request):
    """
    Placeholder main page. Just returns some text.
    """
    return response.text("I'm a teapot", status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)