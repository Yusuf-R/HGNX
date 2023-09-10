from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def endpoint():
    # Get query parameters from the URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    day_of_week = datetime.datetime.now().strftime("%A")

    # Get current UTC time with validation of +/-2 hours
    utc_now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Get GitHub URLs
    file_url = "https://github.com/Yusuf-R/IGNIX/blob/main/0x01-Api/0x01_create_host_api.py"
    source_code_url = "https://github.com/Yusuf-R/IGNIX"

    data = {
        "slack_name": slack_name,
        "day_of_week": day_of_week,
        "utc_time": utc_now,
        "track": track,
        "file_url": file_url,
        "source_code_url": source_code_url,
        "status_code": 200,
    }

    return jsonify(data), 200


if __name__ == "__main__":
    app.run()
