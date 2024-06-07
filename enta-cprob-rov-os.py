from flask import Flask, render_template, request
import smbus
import RPi.GPIO as GPIO
import time

# I2C address of the Arduino
I2C_ADDRESS = 0x04

# Get I2C bus
# bus = smbus.SMBus(1)

# Create Flask app
app = Flask(__name__)

# Definitions
MINIUM_SPEED = 70

# floodSensor
FLOOD_SENSOR_PIN = 10
# Set Vertical propulsors GPIO pins
MOTOR_FL_PIN_A = 22  
MOTOR_FL_PIN_B = 23
MOTOR_FR_PIN_A = 17
MOTOR_FR_PIN_B = 27
MOTOR_BL_PIN_A = 16
MOTOR_BL_PIN_B = 12
MOTOR_BR_PIN_A = 20
MOTOR_BR_PIN_B = 21
# Set Horizontal propulsors GPIO pins
MOTOR_RL_PIN_A = 19
MOTOR_RL_PIN_B = 26
MOTOR_RR_PIN_A = 6
MOTOR_RR_PIN_B = 13
# Set Lighth ON/OFF GPIO pin
LIGHT_PIN = 4

# Set SCL SDA pins
SCL_PIN = 3
SDA_PIN = 2

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

# Set up GPIO flood sensor pin mode
GPIO.setup(FLOOD_SENSOR_PIN, GPIO.IN)


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

def stop_motors():
  pwm_FL_A.stop()
  pwm_FL_B.stop()
  pwm_FR_A.stop()
  pwm_FR_B.stop()
  pwm_BL_A.stop()
  pwm_BL_B.stop()
  pwm_BR_A.stop()
  pwm_BR_B.stop()
  pwm_RL_A.stop()
  pwm_RL_B.stop()
  pwm_RR_A.stop()
  pwm_RR_B.stop()  

# Read data from Arduino via I2C
def read_i2c_data():
    data = bus.read_i2c_block_data(I2C_ADDRESS, 0, 32)
    return ''.join(chr(i) for i in data if i != 0)

# Check flood sensor
def check_flood_sensor():
  if GPIO.input(FLOOD_SENSOR_PIN):
    return False
  else:
    print("Floode Alert!")
    return True

# Set up PWM for propulsors
def set_motor(motorPWM_A, motorPWM_B, speed, direction):
  
  if speed > 100:
    speed = 100
  elif speed < -100:
    speed = -100
  
  # Set motor direction
  if direction == "U":
    motorPWM_A.ChangeDutyCycle(abs(speed))
    motorPWM_B.ChangeDutyCycle(0)

  elif direction == "D":
    motorPWM_A.ChangeDutyCycle(0)
    motorPWM_B.ChangeDutyCycle(abs(speed))
    
  elif direction == "F":
    motorPWM_A.ChangeDutyCycle(abs(speed))
    motorPWM_B.ChangeDutyCycle(0)
  
  elif direction == "R":
    motorPWM_A.ChangeDutyCycle(0)
    motorPWM_B.ChangeDutyCycle(abs(speed))
  
  
def set_ligths(status):
  GPIO.output(LIGHT_PIN, status)
  return  "OK"
      
def vertical_control(direction="U", spd=60):
  set_motor(pwm_FL_A, pwm_FL_B, spd, direction)
  set_motor(pwm_FR_A, pwm_FR_B, spd, direction)
  set_motor(pwm_BL_A, pwm_BL_B, spd, direction)
  set_motor(pwm_BR_A, pwm_BR_B, spd, direction)
  return "OK"
  
def horizontal_control(direction="R", spd=60):
  set_motor(pwm_RL_A, pwm_RL_B, spd, direction)
  set_motor(pwm_RR_A, pwm_RR_B, spd, direction)
  return "OK"
  
def emergency_stop():
  print("Emergency Stop!")
  vertical_control("U", 0)
  vertical_control("U", 0)
  horizontal_control("R", 0)
  horizontal_control("R", 0)
  return "OK"

def stopFR():
  horizontal_control("R", 0)
  horizontal_control("R", 0)
  return "OK"
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    
    motorFL_BL    = float(request.form['motorA'])
    motorBL_BR    = float(request.form['motorB'])
  
    print("motorFL_BL: ", motorFL_BL)
    
    if motorFL_BL > 0:
      vertical_control("U", motorFL_BL)
      vertical_control("U", motorBL_BR)
    else:
      vertical_control("D", motorFL_BL)
      vertical_control("D", motorBL_BR)
  
    return "OK"

@app.route('/emergency', methods=['POST'])
def emergency():
    emergency_stop()
    return "OK"
  
@app.route('/forward', methods=['POST'])
def forward():
    horizontal_control("F", 80)
    return "OK"
  
@app.route('/backward', methods=['POST'])
def backward():
    horizontal_control("R", 80)
    return "OK"
  
@app.route('/stop', methods=['POST'])
def stop():
    stopFR()
    return "OK"

@app.route('/light', methods=['POST'])
def lights():

    status = request.form['status']
    if status == "1":
      set_ligths(True)
    else:
      set_ligths(False)


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=8080)
        while True:
          check_flood_sensor()
    except KeyboardInterrupt:
        pass
    finally:
      set_ligths(False)
      stop_motors()
      GPIO.cleanup()
