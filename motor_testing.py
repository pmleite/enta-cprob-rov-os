import RPi.GPIO as GPIO
import time

# Set up GPIO pins
Motor1A = 17
Motor1B = 27
Motor2A = 22
Motor2B = 23

Motor3A = 12
Motor3B = 16
Motor4A = 20
Motor4B = 21

Motor5A = 6
Motor5B = 13
Motor6A = 19
Motor6B = 26

# GPIO setup
GPIO.setmode(GPIO.BCM)    # Use BCM pin numbering
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor3A, GPIO.OUT)
GPIO.setup(Motor3B, GPIO.OUT)
GPIO.setup(Motor4A, GPIO.OUT)
GPIO.setup(Motor4B, GPIO.OUT)
GPIO.setup(Motor5A, GPIO.OUT)
GPIO.setup(Motor5B, GPIO.OUT)
GPIO.setup(Motor6A, GPIO.OUT)
GPIO.setup(Motor6B, GPIO.OUT)

# Set up PWM on the GPIO pins
pwm1A = GPIO.PWM(Motor1A, 100)  # PWM with 100Hz frequency on Motor1A
pwm1B = GPIO.PWM(Motor1B, 100)  # PWM with 100Hz frequency on Motor1B
pwm2A = GPIO.PWM(Motor2A, 100)  # PWM with 100Hz frequency on Motor2A
pwm2B = GPIO.PWM(Motor2B, 100)  # PWM with 100Hz frequency on Motor2B
pwm3A = GPIO.PWM(Motor3A, 100)  # PWM with 100Hz frequency on Motor1A
pwm3B = GPIO.PWM(Motor3B, 100)  # PWM with 100Hz frequency on Motor1B
pwm4A = GPIO.PWM(Motor4A, 100)  # PWM with 100Hz frequency on Motor2A
pwm4B = GPIO.PWM(Motor4B, 100)  # PWM with 100Hz frequency on Motor2B
pwm5A = GPIO.PWM(Motor5A, 100)  # PWM with 100Hz frequency on Motor1A
pwm5B = GPIO.PWM(Motor5B, 100)  # PWM with 100Hz frequency on Motor1B
pwm6A = GPIO.PWM(Motor6A, 100)  # PWM with 100Hz frequency on Motor2A
pwm6B = GPIO.PWM(Motor6B, 100)  # PWM with 100Hz frequency on Motor2B

# Start PWM with a duty cycle of 0 (motors off)
pwm1A.start(0)
pwm1B.start(0)
pwm2A.start(0)
pwm2B.start(0)
pwm3A.start(0)
pwm3B.start(0)
pwm4A.start(0)
pwm4B.start(0)
pwm5A.start(0)
pwm5B.start(0)
pwm6A.start(0)
pwm6B.start(0)


def set_motor1_speed(speed):
    if speed > 0:
        pwm1A.ChangeDutyCycle(speed)
        pwm1B.ChangeDutyCycle(0)
    else:
        pwm1A.ChangeDutyCycle(0)
        pwm1B.ChangeDutyCycle(-speed)

def set_motor2_speed(speed):
    if speed > 0:
        pwm2A.ChangeDutyCycle(speed)
        pwm2B.ChangeDutyCycle(0)
    else:
        pwm2A.ChangeDutyCycle(0)
        pwm2B.ChangeDutyCycle(-speed)

def set_motor3_speed(speed):
    if speed > 0:
        pwm3A.ChangeDutyCycle(speed)
        pwm3B.ChangeDutyCycle(0)
    else:
        pwm3A.ChangeDutyCycle(0)
        pwm3B.ChangeDutyCycle(-speed)
        
def set_motor4_speed(speed):
    if speed > 0:
        pwm4A.ChangeDutyCycle(speed)
        pwm4B.ChangeDutyCycle(0)
    else:
        pwm4A.ChangeDutyCycle(0)
        pwm4B.ChangeDutyCycle(-speed)
        
def set_motor5_speed(speed):
    if speed > 0:
        pwm5A.ChangeDutyCycle(speed)
        pwm5B.ChangeDutyCycle(0)
    else:
                pwm5A.ChangeDutyCycle(0)
                pwm5B.ChangeDutyCycle(-speed)
                
def set_motor6_speed(speed):
    if speed > 0:
        pwm6A.ChangeDutyCycle(speed)
        pwm6B.ChangeDutyCycle(0)
    else:
        pwm6A.ChangeDutyCycle(0)
        pwm6B.ChangeDutyCycle(-speed)

def rotate_clockwise():
    set_motor1_speed(100)
    set_motor2_speed(100)
    set_motor3_speed(100)
    set_motor4_speed(100)
    set_motor5_speed(100)
    set_motor6_speed(100)
    
def rotate_counterclockwise():
    set_motor1_speed(-100)
    set_motor2_speed(-100)
    set_motor3_speed(-100)
    set_motor4_speed(-100)
    set_motor5_speed(-100)
    set_motor6_speed(-100)

def stop_motors():
    set_motor1_speed(0)
    set_motor2_speed(0)
    set_motor3_speed(0)
    set_motor4_speed(0)
    set_motor5_speed(0)
    set_motor6_speed(0)

try:
    while True:
        rotate_clockwise()
        time.sleep(5)  # Rotate clockwise for 2 seconds
        stop_motors()
        time.sleep(1)  # Stop for 1 second
        rotate_counterclockwise()
        time.sleep(5)  # Rotate counterclockwise for 2 seconds
        stop_motors()
        time.sleep(1)  # Stop for 1 second
except KeyboardInterrupt:
    pass

# Cleanup
pwm1A.stop()
pwm1B.stop()
pwm2A.stop()
pwm2B.stop()
pwm3A.stop()
pwm3B.stop()
pwm4A.stop()
pwm4B.stop()
pwm5A.stop()
pwm5B.stop()
pwm6A.stop()
pwm6B.stop()
GPIO.cleanup()