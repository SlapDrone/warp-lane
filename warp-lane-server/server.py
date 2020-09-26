"""
server.py

Receives an audio file over HTTP, warps it and sends it back
"""
from datetime import datetime
from pathlib import Path
from typing import List

import aiofiles
from sanic import Sanic
from sanic import response as res
from sanic.log import logger
from sanic_cors import CORS
from src.audio import invert_wav_file
from werkzeug.utils import secure_filename

app = Sanic(__name__)
CORS(app)

# store user uploads here
app.config.UPLOAD_DIR = Path("./received_files")
# serve files from static folder
app.config.SERVE_DIR = Path("./static")
app.config.SERVE_DIR.mkdir(exist_ok=True)
app.static("/static", str(app.config.SERVE_DIR))
# restrict upload file formats
app.config.ALLOWED_MEDIA_TYPES = [
    # 'application/pdf',
    "audio/wav",
    "audio/x-wav",
]
app.config.ALLOWED_FILE_EXTS = [
    # 'pdf',
    "wav"
]
# choose port
app.config.PORT = 8000


async def write_file(path, body):
    async with aiofiles.open(path, "wb") as f:
        await f.write(body)
    f.close()


def valid_file_type(
    file_name: str,
    file_type: str,
    allowed_media_types: List[str] = app.config.ALLOWED_MEDIA_TYPES,
    allowed_file_exts: List[str] = app.config.ALLOWED_FILE_EXTS,
) -> bool:
    file_ext = file_name.split(".")[-1]
    if file_ext in allowed_file_exts and file_type in allowed_media_types:
        return True
    return False


@app.route("/", methods=["GET", "OPTIONS"])
def main(request):
    """
    Placeholder main page. Just returns some text.
    """
    return res.text("I'm a teapot", status=418)


@app.route("/upload", methods=["POST", "GET"])
async def process_upload(request):
    """
    Handle HTTP requests for file uploads, saving these to disk.

    GET request => serves an HTML form for manual upload then... v
    POST        => writes file attribute to app.config.UPLOAD_DIR
    """
    # GET case first
    if request.method == "GET":
        return res.html(
            """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        """,
            status=200,
        )

    # Create upload folder if doesn't exist
    if not Path(app.config.UPLOAD_DIR).exists():
        Path(app.config.UPLOAD_DIR).mkdir(exist_ok=True, parents=True)

    # Ensure a file was sent
    # upload_file = request.files.get('file')
    # if not upload_file:
    if len(request.body) == 0:

        return res.redirect("/?error=no_file")

    # Clean up the filename in case it creates security risks
    filename = secure_filename(request.headers["file-name"])
    file_body = request.body  # the binary file content
    file_content_type = request.headers["content-type"]

    # Ensure the file is a valid type and size, and if so
    # write the file to disk and redirect back to main
    # if not valid_file_type(upload_file.name, upload_file.type):
    if not valid_file_type(filename, file_content_type):
        logger.info(
            "Receive file with " f"name: {filename}, type: {file_content_type}"
        )
        return res.redirect("/?error=invalid_file_type")
    # elif not valid_file_size(upload_file.body):
    #     return res.redirect('/?error=invalid_file_size')
    else:
        # write to disk
        file_path = (
            f"{app.config.UPLOAD_DIR}/"
            f"{str(datetime.now()).replace(' ', '_')}_{filename}"
        )
        await write_file(file_path, file_body)
        # TODO: probably a nicer way to factor this keeping upload and download
        # separate! redirect to separate page to download file?
        # Invert the audio sample and write to a new file
        inverted_file_path = invert_wav_file(
            Path(file_path), app.config.SERVE_DIR
        )
        return res.json({"message": "Success", "file-path": inverted_file_path})
        # return res.redirect(f'/static/{inverted_file_path.parts[-1]}')


@app.route("/download", methods=["GET"])
async def process_download(request):

    file_path = "./" + request.headers["file-path"]

    return await res.file(
        file_path,
        mime_type="audio/x-wav",
        headers={
            "Content-Disposition": 'attachment; filename="inverted.wav"',
            "Content-Type": "audio/x-wav",
        },
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config.PORT)
