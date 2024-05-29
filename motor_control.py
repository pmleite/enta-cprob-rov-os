import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuração dos pinos
MOTOR_A_PIN1 = 20
MOTOR_A_PIN2 = 21
MOTOR_A_ENABLE = 16

MOTOR_B_PIN1 = 19
MOTOR_B_PIN2 = 26
MOTOR_B_ENABLE = 13

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_A_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_A_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_A_ENABLE, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_B_ENABLE, GPIO.OUT)

# Configuração PWM
pwm_a = GPIO.PWM(MOTOR_A_ENABLE, 1000)
pwm_b = GPIO.PWM(MOTOR_B_ENABLE, 1000)
pwm_a.start(0)
pwm_b.start(0)

def set_motor_a(forward, speed):
    if forward:
        GPIO.output(MOTOR_A_PIN1, GPIO.HIGH)
        GPIO.output(MOTOR_A_PIN2, GPIO.LOW)
    else:
        GPIO.output(MOTOR_A_PIN1, GPIO.LOW)
        GPIO.output(MOTOR_A_PIN2, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(speed)

def set_motor_b(forward, speed):
    if forward:
        GPIO.output(MOTOR_B_PIN1, GPIO.HIGH)
        GPIO.output(MOTOR_B_PIN2, GPIO.LOW)
    else:
        GPIO.output(MOTOR_B_PIN1, GPIO.LOW)
        GPIO.output(MOTOR_B_PIN2, GPIO.HIGH)
    pwm_b.ChangeDutyCycle(speed)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    motor = request.form['motor']
    action = request.form['action']
    speed = int(request.form['speed'])
    
    if motor == 'A':
        if action == 'forward':
            set_motor_a(True, speed)
        elif action == 'backward':
            set_motor_a(False, speed)
        elif action == 'stop':
            set_motor_a(True, 0)
    elif motor == 'B':
        if action == 'forward':
            set_motor_b(True, speed)
        elif action == 'backward':
            set_motor_b(False, speed)
        elif action == 'stop':
            set_motor_b(True, 0)
    
    return 'OK'

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        pass
    finally:
        pwm_a.stop()
        pwm_b.stop()
        GPIO.cleanup()