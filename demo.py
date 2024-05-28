from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep
import threading
import pygame
from sensors import read_temperature, read_ph, read_conductivity, read_gyroscope, read_sonar

app = Flask(__name__)

# Configuração dos pinos GPIO
motor_pins = {
    'vertical_left_1': (17, 27),    # (pin_pwm, pin_dir)
    'vertical_left_2': (18, 22),
    'vertical_right_1': (19, 23),
    'vertical_right_2': (20, 24),
    'horizontal_left': (25, 5),
    'horizontal_right': (26, 6)
}

GPIO.setmode(GPIO.BCM)
for pwm_pin, dir_pin in motor_pins.values():
    GPIO.setup(pwm_pin, GPIO.OUT)
    GPIO.setup(dir_pin, GPIO.OUT)
    GPIO.output(pwm_pin, GPIO.LOW)
    GPIO.output(dir_pin, GPIO.LOW)

# Configuração do PWM para cada motor
pwm_motors = {motor: GPIO.PWM(pins[0], 100) for motor, pins in motor_pins.items()}
for pwm in pwm_motors.values():
    pwm.start(0)

def control_motor(motor, speed):
    if motor in pwm_motors:
        pwm_pin, dir_pin = motor_pins[motor]
        if speed < 0:
            GPIO.output(dir_pin, GPIO.HIGH)
            pwm_motors[motor].ChangeDutyCycle(abs(speed))
        else:
            GPIO.output(dir_pin, GPIO.LOW)
            pwm_motors[motor].ChangeDutyCycle(speed)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensors')
def sensors():
    data = {
        "temperature": read_temperature(),
        "ph": read_ph(),
        "conductivity": read_conductivity(),
        "gyroscope": read_gyroscope(),
        "sonar": read_sonar()
    }
    return jsonify(data)

def initialize_joystick():
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick
    else:
        return None

def read_joystick_events(joystick):
    pygame.event.pump()
    axis_0 = joystick.get_axis(0)  # Horizontal axis
    axis_1 = joystick.get_axis(1)  # Vertical axis
    axis_2 = joystick.get_axis(2)  # Secondary Horizontal axis
    axis_3 = joystick.get_axis(3)  # Secondary Vertical axis

    return {
        'horizontal': axis_0,
        'vertical': axis_1,
        'secondary_horizontal': axis_2,
        'secondary_vertical': axis_3
    }

def joystick_control():
    joystick = initialize_joystick()
    if not joystick:
        print('No joystick detected')
        return

    while True:
        axes = read_joystick_events(joystick)
        
        # Mapping -1..1 to -100..100
        horizontal_speed = int(axes['horizontal'] * 100)
        vertical_speed = int(axes['vertical'] * 100)
        secondary_horizontal_speed = int(axes['secondary_horizontal'] * 100)
        secondary_vertical_speed = int(axes['secondary_vertical'] * 100)

        # Control horizontal motors
        control_motor('horizontal_left', horizontal_speed)
        control_motor('horizontal_right', horizontal_speed)
        
        # Control vertical motors
        control_motor('vertical_left_1', vertical_speed)
        control_motor('vertical_left_2', vertical_speed)
        control_motor('vertical_right_1', vertical_speed)
        control_motor('vertical_right_2', vertical_speed)
        
        sleep(0.1)

if __name__ == '__main__':
    joystick_thread = threading.Thread(target=joystick_control)
    joystick_thread.start()
    
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)