from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/greet")
def index():
    return "<p>Now everyone can be a hero...</p>"


@app.route("/health")
def health():
    return ("OK", 200)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
