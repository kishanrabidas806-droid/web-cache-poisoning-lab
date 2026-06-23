from flask import Flask, request
import requests

app = Flask(__name__)

cache = {}

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy(path):

    key = request.full_path

    if key in cache:
        return cache[key]

    url = f"http://127.0.0.1:5000/{path}"

    resp = requests.get(
        url,
        headers=request.headers
    )

    cache[key] = resp.text

    return resp.text

if __name__ == "__main__":
    app.run(port=4001)