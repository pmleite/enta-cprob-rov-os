#!/usr/bin/env python3
import serial
import time
import subprocess

SENSOR_SERIAL_PORT  = '/dev/ttyACM0'
ACTUATE_SERIAL_PORT = '/dev/ttyACM1'

SENSOR_COMM_SPEED   = 19200
ACTUATE_COMM_SPEED  = 19200

def main():
    
    #Start video stream sub-process
    try:
        subprocess.Popen(["libcamera-vid", "-n", "-t",  "0", "--inline", "--listen",  "-o", "tcp://0.0.0.0:8888"])
        print("Video Stream iniciado com sucesso!")
    except:
        print("Erro ao iniciar o video stream.")
        print("Verifique o compoenente libcamera-vid e tente novamente")

    try:
        try:
            subprocess.Popen(["sudo", "chmod", "777", "/dev/ttyACM0"])
            sensboard = serial.Serial(SENSOR_SERIAL_PORT, SENSOR_COMM_SPEED, timeout=1)
            print("Placa de sensores inicializada com sucesso!")
        except:
            print("Erro ao inicializar a comunicação com a placa de sensores.")
            print("Verifique e tente novamente.")
    
        try:
            subprocess.Popen(["sudo", "chmod", "777", "/dev/ttyACM1"])
            actuateboard = serial.Serial(ACTUATE_SERIAL_PORT, ACTUATE_COMM_SPEED, timeout=1)
            print("Placa de atuadores inicializada com sucesso!")
        except:
            print("Erro ao inicializar a comunicação com a placa de atuadores.")
            print("Verifique e tente novamente.")
    except:
        print("Erro de inicialização de comunicação com os periféricos!")
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
    


    
