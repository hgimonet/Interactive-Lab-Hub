import time
import board
import busio
import adafruit_mpu6050
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# mpu.reset()

dt=0.001
num_measurements = 10000
count = 0

accel_recordings = []
gyro_recordings = []

while count < num_measurements:
    accel_recordings.append(np.array(mpu.acceleration))
    gyro_recordings.append(np.array(mpu.gyro))
    time.sleep(dt)

accel_recordings = np.array(accel_recordings)
print(accel_recordings.shape)

# while True:
#     print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
#     print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
#     # print("Temperature: %.2f C"%mpu.temperature)
#     print("")
#
#     time.sleep(1)