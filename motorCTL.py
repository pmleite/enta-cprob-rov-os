# motor_control.py
import pigpio

# Initialize pigpio
pi = pigpio.pi()

# Motor control function
def set_motor_speed(motor, speed):
    # Convert speed to PWM range
    pwm_value = int((speed + 100) * 2.55)
    if speed < 0:
        pi.set_PWM_dutycycle(motor, 255 - pwm_value)  # Reverse direction
    else:
        pi.set_PWM_dutycycle(motor, pwm_value)

# Example: Set motor 1 to speed 50
set_motor_speed(17, 50)  # GPIO pin 17