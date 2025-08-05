from flask import Flask, render_template, jsonify
import pandas as pd
import time

app = Flask(__name__)

# Load test lap data (fast lap)
telemetry_data = pd.read_csv("simulated_telemetry_fast_lap.csv")
telemetry_data = telemetry_data.to_dict(orient="records")

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/telemetry")
def get_telemetry():
    # Cycle through data like it's live
    index = int(time.time() * 10) % len(telemetry_data)
    return jsonify(telemetry_data[index])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)