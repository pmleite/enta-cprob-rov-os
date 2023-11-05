#!/usr/bin/env python3
import serial
import time

SENSOR_SERIAL_PORT  = '/dev/ttyACM0'
ACTUATE_SERIAL_PORT = '/dev/ttyACM1'

SENSOR_COMM_SPEED   = 19200
ACTUATE_COMM_SPEED  = 19200

def main():
    
    try:
        sensboard = serial.Serial(SENSOR_SERIAL_PORT, SENSOR_COMM_SPEED, timeout=1)
        actuateboard = serial.Serial(ACTUATE_SERIAL_PORT, ACTUATE_COMM_SPEED, timeout=1)
    except:
        print("One or more arduino boards are not connected.")
        print("Please check you connections and try again.")
        exit()
        
    sensboard.reset_input_buffer()
    actuateboard.reset_input_buffer()
    
    while True:    
        # Send data to actuateboard
        actuateboard.write(b"LETS TALK!\n")
        # Read data from sensboard
        line = sensboard.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

if __name__ == '__main__':
    main()
    


    
