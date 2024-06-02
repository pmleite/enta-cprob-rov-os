from flask import Flask, render_template, Response, request
import RPi.GPIO as GPIO
import cv2
import time

# Definitions
MINIUM_SPEED = 70
tTCP_PORT    = 5000

# Set up Flask app
app = Flask(__name__)

# Video capture
camera = cv2.VideoCapture(0)

# floodSensor
FLOOD_SENSOR_PIN = 10
# Set Vertical propulsors GPIO pins
MOTOR_FL_PIN_A = 22  
MOTOR_FL_PIN_B = 23
MOTOR_FR_PIN_A = 17
MOTOR_FR_PIN_B = 27
MOTOR_BL_PIN_A = 16
MOTOR_BL_PIN_B = 12
MOTOR_BR_PIN_A = 21
MOTOR_BR_PIN_B = 20
# Set Horizontal propulsors GPIO pins
MOTOR_RL_PIN_A = 19
MOTOR_RL_PIN_B = 26
MOTOR_RR_PIN_A = 6
MOTOR_RR_PIN_B = 13
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


# Check flood sensor
def check_flood_sensor():
  if GPIO.input(FLOOD_SENSOR_PIN):
    return False
  else:
    print("Floode Alert!")
    return True

# Set up PWM for propulsors
def set_motor(motorPWM_A, motorPWM_B, speed, direction):
  
  # Check if speed is lower than MINIUM_SPEED
  if speed < MINIUM_SPEED:
    speed = MINIUM_SPEED
  
  # Set motor direction
  if direction == "U":
    motorPWM_A.ChangeDutyCycle(speed)
    motorPWM_B.ChangeDutyCycle(0)
  else:
    motorPWM_A.ChangeDutyCycle(0)
    motorPWM_B.ChangeDutyCycle(speed)
  
    
def set_ligths(status):
  GPIO.output(LIGHT_PIN, status)
      
def vertical_control(direction="U"):
  set_motor(pwm_FL_A, pwm_FL_B, 60, direction)
  set_motor(pwm_FR_A, pwm_FR_B, 60, direction)
  set_motor(pwm_BL_A, pwm_BL_B, 60, direction)
  set_motor(pwm_BR_A, pwm_BR_B, 60, direction)
  
def horizontal_control(direction="R"):
  set_motor(pwm_RL_A, pwm_RL_B, 60, direction)
  set_motor(pwm_RR_A, pwm_RR_B, 60, direction)


def genFrames():
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Video streaming
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
  try:
    while True:
      app.run(host='0.0.0.0', port=tcp_port)
      vertical_control("U")
      horizontal_control("F")
      set_ligths(True)
      check_flood_sensor()
  except KeyboardInterrupt:
      pass
      set_ligths(False)
      stop_motors()
      GPIO.cleanup()