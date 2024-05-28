import asyncio
import websockets
import json
import RPi.GPIO as GPIO

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

async def joystick_handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        horizontal_speed = int(data['horizontal'] * 100)
        vertical_speed = int(data['vertical'] * 100)
        secondary_horizontal_speed = int(data['secondary_horizontal'] * 100)
        secondary_vertical_speed = int(data['secondary_vertical'] * 100)

        # Control horizontal motors
        control_motor('horizontal_left', horizontal_speed)
        control_motor('horizontal_right', horizontal_speed)
        
        # Control vertical motors
        control_motor('vertical_left_1', vertical_speed)
        control_motor('vertical_left_2', vertical_speed)
        control_motor('vertical_right_1', vertical_speed)
        control_motor('vertical_right_2', vertical_speed)

start_server = websockets.serve(joystick_handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()