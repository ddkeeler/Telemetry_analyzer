import socket
import struct
import time
import csv

# === Set up UDP socket ===
UDP_IP = "0.0.0.0"
UDP_PORT = 9996
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for ACC telemetry on UDP port {UDP_PORT}...")

with open("simulated_telemetry_slow_lap.csv", "r") as f:
    reader = csv.DictReader(f)
    telemetry_log = list(reader)

for row in telemetry_log:
    print(row)  # You can later analyze or visualize this


# === Packet Parser ===
def parse_packet(data):
    try:
        # Simplified: parse 8 values (32 bytes total)
        speed, throttle, brake, clutch, gear, rpm, steer, lap_time = struct.unpack('ffffifff', data[:32])
        return {
            "timestamp": time.time(),
            "speed_kph": speed * 3.6,   # Convert m/s to km/h
            "throttle": throttle,
            "brake": brake,
            "clutch": clutch,
            "gear": gear,
            "rpm": rpm,
            "steer": steer,
            "lap_time": lap_time
        }
    except Exception as e:
        print("Packet decode failed:", e)
        return None

# === Storage ===
telemetry_log = []

# === Main Loop ===
try:
    while True:
        data, addr = sock.recvfrom(1024)
        parsed = parse_packet(data)
        if parsed:
            telemetry_log.append(parsed)
            print(parsed)
except KeyboardInterrupt:
    print("\nSession ended. Saving data...")
    keys = telemetry_log[0].keys()
    with open("acc_session_log.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(telemetry_log)
    print("Saved to acc_session_log.csv")
