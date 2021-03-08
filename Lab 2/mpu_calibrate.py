import time
import board
import busio
import adafruit_mpu6050
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# mpu.reset()

dt=0.001
secs = 5.0
num_measurements = int(secs/dt)
count = 0

accel_recordings = []
gyro_recordings = []

print('Will measure for %.1f seconds, do not move sensor.'%(secs))
while count < num_measurements:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    accel_recordings.append(np.array(mpu.acceleration))
    gyro_recordings.append(np.array(mpu.gyro))
    time.sleep(dt)
    count +=1

print(np.array(accel_recordings).mean(axis=0))
print(np.array(gyro_recordings).mean(axis=0))