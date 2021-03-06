import time
import board
import busio
import adafruit_mpu6050
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)


v = np.zeros(3)
dt = 1

while True:
    # calculate velocity
    v += np.array(mpu.acceleration)*dt
    speed = np.linalg.norm(v)

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    print("Speed: X:%.2f, Y: %.2f, Z: %.2f m/s^2" %v)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
    print("Temperature: %.2f C"%mpu.temperature)
    print("")

    time.sleep(dt)