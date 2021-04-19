import time
import board
import busio
import adafruit_mpu6050
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)


accel_offsets = [ 0.82114222, -0.13894366,  7.9939099 ]
gyro_offsets = [-2.36665191, -0.4468687,  -0.18727176]

accel_data = []
window = 10
thresh = 20.


while True:
    accel = np.array(mpu.acceleration) - accel_offsets
    gyro = np.array(mpu.gyro) - gyro_offsets
    accel = mpu.acceleration
    accel_data.append(accel)

    accel_window = np.array(accel_data[-window:])
    # Set up threshold detection
    above_thresh = accel > thresh
    # Set up averaging
    moving_avg = np.mean(accel_window)
    # Set up peak detection
    peaks = sg.find_peaks(accel_window)
    print(above_thresh, moving_avg, peaks, end="\r")

    time.sleep(dt)