from gpiozero import PWMOutputDevice, DigitalOutputDevice
from time import sleep

# Define motor control pins
PWM_PIN = 27
IN1_PIN = 17
IN2_PIN = 22

# Initialize the motor control pins
motor_pwm = PWMOutputDevice(PWM_PIN)
motor_in1 = DigitalOutputDevice(IN1_PIN)
motor_in2 = DigitalOutputDevice(IN2_PIN)

def motor_forward(speed):
    motor_in1.on()
    motor_in2.off()
    motor_pwm.value = speed

def motor_backward(speed):
    motor_in1.off()
    motor_in2.on()
    motor_pwm.value = speed

def motor_stop():
    motor_in1.off()
    motor_in2.off()
    motor_pwm.value = 0

try:
    while True:
        print("Motor forward at full speed")
        motor_forward(100)
        
except KeyboardInterrupt:
    print("Program stopped")
    motor_stop()
