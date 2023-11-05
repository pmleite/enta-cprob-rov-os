#!/usr/bin/env python3
SENSBOARD_PORT    ='/dev/ttyACM0'
ACTUATEBOARD_PORT ='/dev/ttyACM1'

import serial

if __name__ == '__main__':
    ser = serial.Serial(SENSBOARD_PORT, 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)