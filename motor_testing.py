import RPi.GPIO as GPIO
  

# Configuração dos pinos
MOTOR_FL_PIN1   = 17
MOTOR_FL_PIN2   = 22
MOTOR_FL_PWM    = 27

MOTOR_FR_PIN1   = 23
MOTOR_FR_PIN2   = 24
MOTOR_FR_PWM    = 25

MOTOR_BL_PIN1   = 21
MOTOR_BL_PIN2   = 20
MOTOR_BL_PWM    = 16

MOTOR_BR_PIN1   = 13
MOTOR_BR_PIN2   = 19
MOTOR_BR_PWM    = 26

# GPIO Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_FL_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_FL_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_FL_PWM,  GPIO.OUT)
GPIO.setup(MOTOR_FR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_FR_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_FR_PWM,  GPIO.OUT)
GPIO.setup(MOTOR_BL_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_BL_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_BL_PWM,  GPIO.OUT)
GPIO.setup(MOTOR_BR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_BR_PIN2, GPIO.OUT)
GPIO.setup(MOTOR_BR_PWM,  GPIO.OUT)
print("GPIO Configured")

# PWM Initialization
pwm_1 = GPIO.PWM(MOTOR_FL_PWM, 100)
pwm_2 = GPIO.PWM(MOTOR_FR_PWM, 100)
pwm_3 = GPIO.PWM(MOTOR_BL_PWM, 100)
pwm_4 = GPIO.PWM(MOTOR_BR_PWM, 100)
print("PWM Initialized")
pwm_1.start(0)
pwm_2.start(0)
pwm_3.start(0)
pwm_4.start(0)
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
        set_motor((MOTOR_FL_PIN1, MOTOR_FL_PIN2, pwm_1), 50)
        set_motor((MOTOR_FR_PIN1, MOTOR_FR_PIN2, pwm_2), 100)
        set_motor((MOTOR_BL_PIN1, MOTOR_BL_PIN2, pwm_3), 100)
        set_motor((MOTOR_BR_PIN1, MOTOR_BR_PIN2, pwm_4), 100)


if __name__ == "__main__":
    try:
        teste()
    except KeyboardInterrupt:
        pass
    finally:
        print("Cleaning up")
        pwm_1.stop()
        pwm_2.stop()
        pwm_3.stop()
        pwm_4.stop()
        GPIO.cleanup()
        print("Program Finished")

    
        
    









