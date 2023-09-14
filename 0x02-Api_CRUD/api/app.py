#!/usr/bin/env python3
"""Template for the user app"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def shutdown(self):
    """Flask shutdown function"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Create a handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5800, debug=True)
