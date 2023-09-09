#!/usr/bin/env python3
"""Create host api."""
from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def endpoint():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    day_of_week = datetime.datetime.now().strftime("%A")

    # Get current UTC time with validation of +/-2 hours
    utc_now = datetime.datetime.now(pytz.utc)
    utc_offset = utc_now.utcoffset().total_seconds() / 3600

    if utc_offset < -2 or utc_offset > 2:
        return jsonify({"error": "Invalid UTC offset"}), 400

    # Get GitHub URLs
    file_url = 'https://github.com/Yusuf-R/IGNIX/'
    source_code_url = 'https://github.com/your_username/your_repository'

    response = {
        "slack_name": slack_name,
        "day_of_week": day_of_week,
        "utc_time": utc_now.strftime("%Y-%m-%d %H:%M:%S"),
        "track": track,
        "file_url": file_url,
        "source_code_url": source_code_url
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

