from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    original_host = request.host

    host = request.headers.get(
        "X-Forwarded-Host",
        original_host
    )

    solved = ""

    if host != original_host:
        solved = f"""
        <div style="background:green;color:white;padding:10px">
            🎉 LAB SOLVED!
            <br>
            Poisoned Host: {host}
        </div>
        """

    return f"""
    <html>
    <body>

    {solved}

    <h1>Welcome</h1>

    <script src="http://{host}/static/app.js"></script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(port=5000)