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

MOTOR_C_PIN1 = 31
MOTOR_C_PIN2 = 32
MOTOR_C_ENABLE = 29

MOTOR_D_PIN1 = 7
MOTOR_D_PIN2 = 8
MOTOR_D_ENABLE = 1

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_A_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_A_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_A_ENABLE, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_B_ENABLE, GPIO.OUT)
GPIO.setup(MOTOR_C_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_C_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_C_ENABLE, GPIO.OUT)
GPIO.setup(MOTOR_D_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_D_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_D_ENABLE, GPIO.OUT)


# Configuração PWM
pwm_a = GPIO.PWM(MOTOR_A_ENABLE, 1000)
pwm_b = GPIO.PWM(MOTOR_B_ENABLE, 1000)
pwm_c = GPIO.PWM(MOTOR_C_ENABLE, 1000)
pwm_d = GPIO.PWM(MOTOR_D_ENABLE, 1000)
pwm_a.start(0)
pwm_b.start(0)
pwm_c.start(0)
pwm_d.start(0)

def set_motor(motor_pins, speed):
   
    pin1, pin2, pwm = motor_pins
   
    if speed >= 0:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
    else:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.HIGH)
    
    pwm.ChangeDutyCycle(abs(speed))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    motor_a_speed = float(request.form['motorA'])
    motor_b_speed = float(request.form['motorB'])
    motor_c_speed = float(request.form['motorA'])
    motor_d_speed = float(request.form['motorB'])

    set_motor((MOTOR_A_PIN1, MOTOR_A_PIN2, pwm_a), motor_a_speed)
    set_motor((MOTOR_B_PIN1, MOTOR_B_PIN2, pwm_b), motor_b_speed)
    set_motor((MOTOR_C_PIN1, MOTOR_C_PIN2, pwm_c), motor_c_speed)
    set_motor((MOTOR_D_PIN1, MOTOR_D_PIN2, pwm_d), motor_d_speed)
    
    return 'OK'

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        pass
    finally:
        pwm_a.stop()
        pwm_b.stop()
        pwm_c.stop()
        pwm_d.stop()
        GPIO.cleanup()