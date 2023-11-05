#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    sensboard    = serial.Serial('/dev/ttyACM0', 19200, timeout=1)
    actuateboard = serial.Serial('/dev/ttyACM1', 19200, timeout=1)
    
    sensboard.reset_input_buffer()
    actuateboard.reset_input_buffer()
    
    while True:
        
        # Send data to actuateboard
        actuateboard.write(b"LETS TALK!\n")
        # Read data from sensboard
        line = sensboard.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)