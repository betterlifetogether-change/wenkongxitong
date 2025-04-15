import time
import random

# 模拟温度传感器读取水温
def read_temperature():
    return random.uniform(20, 50)

# 模拟水位传感器读取水位
def read_water_level():
    return random.uniform(0, 100)

while True:
    temperature = read_temperature()
    water_level = read_water_level()
    print(f"Temperature: {temperature} °C, Water Level: {water_level}%")
    time.sleep(1)
