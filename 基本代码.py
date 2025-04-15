import time

# PID控制器类
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

# 模拟传感器读取水温
def read_temperature():
    # 这里只是模拟，实际应用中需要读取传感器数据
    import random
    return random.uniform(20, 50)

# 模拟执行器调节水温
def adjust_temperature(power):
    # 这里只是模拟，实际应用中需要控制加热或冷却设备
    print(f"Adjusting temperature with power: {power}")

# 主程序
if __name__ == "__main__":
    setpoint = 40  # 目标水温
    Kp = 1.0
    Ki = 0.1
    Kd = 0.01
    pid = PIDController(Kp, Ki, Kd)

    while True:
        current_temperature = read_temperature()
        print(f"Current temperature: {current_temperature}")
        power = pid.update(setpoint, current_temperature)
        adjust_temperature(power)
        time.sleep(1)
