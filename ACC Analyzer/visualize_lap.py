"""
visualize_lap.py

This script compares telemetry data between a fast lap and a slow lap using CSV files.
It visualizes speed, throttle, and brake inputs over time for both laps.

Usage:
- Place 'simulated_telemetry_fast_lap.csv' and 'simulated_telemetry_slow_lap.csv' in the same directory.
- Each CSV should contain columns: 'timestamp', 'speed_kph', 'throttle', 'brake'.

Run the script to display comparison plots for speed, throttle, and brake inputs.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Check if CSV files exist
fast_lap_path = "simulated_telemetry_fast_lap.csv"
slow_lap_path = "simulated_telemetry_slow_lap.csv"

if not os.path.isfile(fast_lap_path) or not os.path.isfile(slow_lap_path):
	print(f"Error: One or both telemetry CSV files are missing.\n"
		  f"Expected files:\n - {fast_lap_path}\n - {slow_lap_path}\n"
		  "Please ensure both files are present in the script directory.")
	sys.exit(1)

# Load your telemetry CSVs
fast_lap_df = pd.read_csv(fast_lap_path)
slow_lap_df = pd.read_csv(slow_lap_path)

# Ensure timestamp is numeric
fast_lap_df["timestamp"] = fast_lap_df["timestamp"].astype(float)
slow_lap_df["timestamp"] = slow_lap_df["timestamp"].astype(float)

# Plot Speed Comparison
plt.figure(figsize=(12, 4))
plt.plot(fast_lap_df["timestamp"], fast_lap_df["speed_kph"], label="Fast Lap", color="green")
plt.plot(slow_lap_df["timestamp"], slow_lap_df["speed_kph"], label="Slow Lap", color="red")
plt.title("Speed vs Time Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Speed (kph)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot Throttle Comparison
plt.figure(figsize=(12, 4))
plt.plot(fast_lap_df["timestamp"], fast_lap_df["throttle"], label="Fast Lap Throttle", linestyle="--", color="green")
plt.plot(slow_lap_df["timestamp"], slow_lap_df["throttle"], label="Slow Lap Throttle", linestyle="--", color="red")
plt.title("Throttle Input Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Throttle (0.0 - 1.0)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot Brake Comparison
plt.figure(figsize=(12, 4))
plt.plot(fast_lap_df["timestamp"], fast_lap_df["brake"], label="Fast Lap Brake", linestyle=":", color="green")
plt.plot(slow_lap_df["timestamp"], slow_lap_df["brake"], label="Slow Lap Brake", linestyle=":", color="red")
plt.title("Brake Input Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Brake (0.0 - 1.0)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
