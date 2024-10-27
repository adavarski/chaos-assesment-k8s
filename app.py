from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route("/greet")
def index():
    # Get the 'name' query parameter
    name = request.args.get("name")
    if name:
        # Return JSON response with the name included
        return jsonify({"message": f"Hello {name}!"})
    else:
        # Default message if name is not provided
        return jsonify({"message": "Now everyone can be a hero..."})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
