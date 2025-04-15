import time
import random

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, setpoint, current_value):
        error = setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# 模拟执行器调节水温
def adjust_temperature(power):
    print(f"Adjusting temperature with power: {power}")

setpoint = 40 # 目标水温
Kp = 1.0
Ki = 0.1
Kd = 0.01
pid = PIDController(Kp, Ki, Kd)

while True:
    current_temperature = read_temperature()
    power = pid.update(setpoint, current_temperature)
    adjust_temperature(power)
    time.sleep(1)
