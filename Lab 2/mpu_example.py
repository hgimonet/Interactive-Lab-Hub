import time
import board
import busio
import adafruit_mpu6050
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)


accel_offsets = [ 0.82114222, -0.13894366,  7.9939099 ]
gyro_offsets = [-2.36665191, -0.4468687,  -0.18727176]

v = np.zeros(3)
gravity = np.array([0,0,1]) * 9.8
dt = 0.10



while True:
    accel = np.array(mpu.acceleration) - accel_offsets
    gyro = np.array(mpu.gyro) - gyro_offsets
    # calculate velocity
    v += accel*dt
    speed = np.linalg.norm(v)

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(tuple(accel)))
    print("Speed: X:%.2f, Y: %.2f, Z: %.2f m/s^2" %(tuple(v)))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(tuple(gyro)))
    print("Temperature: %.2f C"%mpu.temperature)
    print("")

    time.sleep(dt)