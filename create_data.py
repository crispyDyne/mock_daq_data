import sqlite3
import random
import time
from datetime import datetime


# Function to generate random GPS coordinates
def generate_gps():
    lat = random.uniform(-90.0, 90.0)
    lon = random.uniform(-180.0, 180.0)
    alt = random.uniform(0, 1000)  # Altitude in meters
    return lat, lon, alt


# Function to generate random accelerometer and gyroscope data
def generate_accel_gyro():
    accel = [random.uniform(-10, 10) for _ in range(3)]  # X, Y, Z acceleration
    gyro = [random.uniform(-500, 500) for _ in range(3)]  # X, Y, Z angular velocity
    return accel, gyro


# Function to generate random DAC values
def generate_dac():
    return [random.uniform(0, 5) for _ in range(4)]  # Four channels with 0-5V range


# Create database and table structure
def create_database():
    conn = sqlite3.connect("data_acquisition.db")
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        latitude REAL,
        longitude REAL,
        altitude REAL,
        accel_x REAL,
        accel_y REAL,
        accel_z REAL,
        gyro_x REAL,
        gyro_y REAL,
        gyro_z REAL,
        dac_1 REAL,
        dac_2 REAL,
        dac_3 REAL,
        dac_4 REAL
    )
    """
    )
    conn.commit()
    conn.close()


# Insert mock data into the database
def insert_mock_data():
    conn = sqlite3.connect("data_acquisition.db")
    cursor = conn.cursor()

    for _ in range(100):  # Generate 100 mock data entries
        timestamp = datetime.now().isoformat()
        lat, lon, alt = generate_gps()
        accel, gyro = generate_accel_gyro()
        dac = generate_dac()

        cursor.execute(
            """
        INSERT INTO sensor_data (
            timestamp, latitude, longitude, altitude,
            accel_x, accel_y, accel_z,
            gyro_x, gyro_y, gyro_z,
            dac_1, dac_2, dac_3, dac_4
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                timestamp,
                lat,
                lon,
                alt,
                accel[0],
                accel[1],
                accel[2],
                gyro[0],
                gyro[1],
                gyro[2],
                dac[0],
                dac[1],
                dac[2],
                dac[3],
            ),
        )

        conn.commit()
        # time.sleep(0.1)  # Simulate a delay between data entries

    conn.close()


# Main function
if __name__ == "__main__":
    create_database()
    insert_mock_data()
    print("Mock data written to 'data_acquisition.db'")
