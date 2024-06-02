import RPi.GPIO as GPIO

# Configuração dos pinos
MOTOR_1_PIN1   = 17
MOTOR_1_PIN2   = 22
MOTOR_1_PWM    = 27

# MOTOR_2_PIN1   = 23
# MOTOR_2_PIN2   = 24
# MOTOR_2_PWM    = 25

# MOTOR_3_PIN1   = 21
# MOTOR_3_PIN2   = 20
# MOTOR_3_PWM    = 16

# MOTOR_4_PIN1   = 13
# MOTOR_4_PIN2   = 19
# MOTOR_4_PWM    = 26

# GPIO Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_1_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_1_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_1_PWM, GPIO.OUT)
# GPIO.setup(MOTOR_2_PIN1, GPIO.OUT)
# GPIO.setup(MOTOR_2_PIN2, GPIO.OUT)
# GPIO.setup(MOTOR_2_PWM, GPIO.OUT)
# GPIO.setup(MOTOR_3_PIN1, GPIO.OUT)
# GPIO.setup(MOTOR_3_PIN2, GPIO.OUT)
# GPIO.setup(MOTOR_3_PWM, GPIO.OUT)
# GPIO.setup(MOTOR_4_PIN1, GPIO.OUT)
# GPIO.setup(MOTOR_4_PIN2, GPIO.OUT)
# GPIO.setup(MOTOR_4_PWM, GPIO.OUT)
print("GPIO Configured")

# PWM Initialization
pwm_1 = GPIO.PWM(MOTOR_1_PWM, 1000)
# pwm_2 = GPIO.PWM(MOTOR_2_PWM, 1000)
# pwm_3 = GPIO.PWM(MOTOR_3_PWM, 1000)
# pwm_4 = GPIO.PWM(MOTOR_4_PWM, 1000)
print("PWM Initialized")
pwm_1.start(0)
# pwm_2.start(0)
# pwm_3.start(0)
# pwm_4.start(0)
print("PWM Started")

def set_motor(motor_pins, speed):
    
        pin1, pin2, pwm = motor_pins
        
        if speed >= 0:
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.LOW)
        else:
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.HIGH)
            
        pwm.ChangeDutyCycle(abs(speed))
        
def teste():  
    # Test
    while True: 
        print("Teste")
        set_motor((MOTOR_1_PIN1, MOTOR_1_PIN2, pwm_1), 1000)
        # set_motor((MOTOR_2_PIN1, MOTOR_2_PIN2, pwm_2), 1000)
        # set_motor((MOTOR_3_PIN1, MOTOR_3_PIN2, pwm_3), 1000)
        # set_motor((MOTOR_4_PIN1, MOTOR_4_PIN2, pwm_4), 1000)


if __name__ == "__main__":
    try:
        teste()
    except KeyboardInterrupt:
        pass
    finally:
        pwm_1.stop()
        # pwm_2.stop()
        # pwm_3.stop()
        # pwm_4.stop()
        GPIO.cleanup()

    
        
    









