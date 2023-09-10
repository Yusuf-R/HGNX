#!/usr/bin/env python3
"""A template for a Flask app"""

from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def endpoint():
    slack_name = request.args.get("slack_name")
    current_day = datetime.datetime.now().strftime("%A")
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    track = request.args.get("track")
    github_file_url = "https://github.com/Yusuf-R/IGNIX/blob/main/0x01-Api/0x01_create_host_api.py"
    github_repo_url = "https://github.com/Yusuf-R/IGNIX"
    status_code = 200

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code,
    }

    ret_data = jsonify(data)
    ret_data.headers["Cotent-Type"] = "application/json"

    return ret_data


if __name__ == "__main__":
    app.run()
