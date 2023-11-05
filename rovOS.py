#!/usr/bin/env python3
import serial
import time

def main():
    
    try:
        sensboard = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        actuateboard = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
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
    


    
