import time
import board
import busio
import adafruit_mpu6050
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# mpu.reset()

dt=0.001
secs = 10.0
num_measurements = int(secs/dt)
count = 0

accel_recordings = []
gyro_recordings = []

print('Will measure for %.1f seconds, do not move sensor.'%(secs))
while count < num_measurements:
    # print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    accel_recordings.append(np.array(mpu.acceleration))
    gyro_recordings.append(np.array(mpu.gyro))
    time.sleep(dt)
    count +=1

# accel_recordings = np.array(accel_recordings)
# accel_recordings = np.array(accel_recordings)
print(np.array(accel_recordings).mean(axis=0))
print(np.array(gyro_recordings).mean(axis=0))

# while True:
#     print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
#     print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
#     # print("Temperature: %.2f C"%mpu.temperature)
#     print("")
#
#     time.sleep(1)