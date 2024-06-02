import RPi.GPIO as GPIO
import time

# Set Vertical propulsors GPIO pins
MOTOR_FL_PIN_A = 22  
MOTOR_FL_PIN_B = 23
MOTOR_FR_PIN_A = 17
MOTOR_FR_PIN_B = 27
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

pwm_FL_A.start(0)
pwm_FL_B.start(0)
pwm_FR_A.start(0)
pwm_FR_B.start(0)
pwm_BL_A.start(0)
pwm_BL_B.start(0)
pwm_BR_A.start(0)
pwm_BR_B.start(0)
pwm_RL_A.start(0)
pwm_RL_B.start(0)
pwm_RR_A.start(0)
pwm_RR_B.start(0)



# Set up PWM for propulsors
def set_motor(motorPinA, motorPinB, speed, direction):
  
  if direction == "U":
    GPIO.output(motorPinA, speed)
    GPIO.output(motorPinB, 0)
  elif direction == "D":
    GPIO.output(motorPinA, 0)
    GPIO.output(motorPinB, speed)
  
    
def set_ligths(status):
  GPIO.output(LIGHT_PIN, status)
      
def control():
  set_motor(MOTOR_FL_PIN_A, MOTOR_FL_PIN_B, 60, "U")


if __name__ == '__main__':
  try:
    while True:
      control()
  except KeyboardInterrupt:
      pass
      pwm_FL_A.stop()
      pwm_FL_B.stop()
      pwm_FR_A.stop()
      pwm_FR_B.stop()
      GPIO.cleanup()