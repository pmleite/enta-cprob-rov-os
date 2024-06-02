import RPi.GPIO as GPIO
import time

# Set Vertical propulsors GPIO pins
MOTOR_FL_PIN_A = 17
MOTOR_FL_PIN_B = 27
MOTOR_FR_PIN_A = 22
MOTOR_FR_PIN_B = 23
MOTOR_BL_PIN_A = 12
MOTOR_BL_PIN_B = 16
MOTOR_BR_PIN_A = 20
MOTOR_BR_PIN_B = 21
# Set Horizontal propulsors GPIO pins
MOTOR_RL_PIN_A = 6
MOTOR_RL_PIN_B = 13
MOTOR_RR_PIN_A = 19
MOTOR_RR_PIN_B = 26
# Set Lighth ON/OFF GPIO pin
LIGHT_PIN = 4

# Set up GPIO pins relative reference
GPIO.setmode(GPIO.BCM)

# Set up GPIO propulsors pins mode
GPIO.setup(MOTOR_FL_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_FL_PIN_B, GPIO.OUT)
GPIO.setup(MOTOR_FR_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_FR_PIN_B, GPIO.OUT)
GPIO.setup(MOTOR_BL_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_BL_PIN_B, GPIO.OUT)
GPIO.setup(MOTOR_BR_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_BR_PIN_B, GPIO.OUT)
GPIO.setup(MOTOR_RL_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_RL_PIN_B, GPIO.OUT)
GPIO.setup(MOTOR_RR_PIN_A, GPIO.OUT)
GPIO.setup(MOTOR_RR_PIN_B, GPIO.OUT)
# Set up GPIO light pin mode
GPIO.setup(LIGHT_PIN, GPIO.OUT)


# Set up PWM for propulsors
pwm_FL_A = GPIO.PWM(MOTOR_FL_PIN_A, 100)
pwm_FL_B = GPIO.PWM(MOTOR_FL_PIN_B, 100)
pwm_FR_A = GPIO.PWM(MOTOR_FR_PIN_A, 100)
pwm_FR_B = GPIO.PWM(MOTOR_FR_PIN_B, 100)
pwm_BL_A = GPIO.PWM(MOTOR_BL_PIN_A, 100)
pwm_BL_B = GPIO.PWM(MOTOR_BL_PIN_B, 100)
pwm_BR_A = GPIO.PWM(MOTOR_BR_PIN_A, 100)
pwm_BR_B = GPIO.PWM(MOTOR_BR_PIN_B, 100)
pwm_RL_A = GPIO.PWM(MOTOR_RL_PIN_A, 100)
pwm_RL_B = GPIO.PWM(MOTOR_RL_PIN_B, 100)
pwm_RR_A = GPIO.PWM(MOTOR_RR_PIN_A, 100)
pwm_RR_B = GPIO.PWM(MOTOR_RR_PIN_B, 100)


# Set up PWM for propulsors
def set_motor(motor_pins, speed):
    
    pin1, pin2, pwm = motor_pins
  
    if speed >= 0:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
    else:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.HIGH)
    pwm.ChangeDutyCycle(abs(speed))
    
def set_ligths(status):
    GPIO.output(LIGHT_PIN, status):
      
def control()
  set_motor((MOTOR_FL_PIN_A, MOTOR_FL_PIN_B, pwm_a), 80)


if __main__ == '__main__':
  try:
    while True:
      control()
  except KeyboardInterrupt:
      pass
      pwm_FL_A.stop()
      pwm_FL_B.stop()
      GPIO.cleanup()