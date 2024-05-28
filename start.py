def main():
    
    #Start video stream sub-process
    try:
        subprocess.Popen(["python3", "videoStreamAndControls"])
        print("Video Stream iniciado com sucesso!")
    except:
        print("Erro ao iniciar o video stream.")
        print("Verifique o compoenente libcamera-vid e tente novamente")

    # #Start sensor and actuator boards comm
    # try:
    #     subprocess.Popen(["sudo", "chmod", "777", "/dev/ttyACM0"])
    #     subprocess.Popen(["sudo", "chmod", "777", "/dev/ttyACM1"])
    #     sensboard = serial.Serial(SENSOR_SERIAL_PORT, SENSOR_COMM_SPEED, timeout=1)
    #     actuateboard = serial.Serial(ACTUATE_SERIAL_PORT, ACTUATE_COMM_SPEED, timeout=1)
    #     print("As placas de sensores e atuadores inicializaram com sucesso!")
    # except:
    #     print("Erro ao inicializar a comunicação com as placas de sensores e atuadores")
    #     print("Verifique e tente novamente.")
    #     exit()

    # sensboard.reset_input_buffer()
    # actuateboard.reset_input_buffer()
    
    #teste de escrita
    
    
    #while True:    
        # # Send data to actuateboard
        # actuateboard.write(b"LETS TALK!\n")
        # Read data from sensboard
        #line = sensboard.readline().decode('utf-8').rstrip()
       
        # line = sensboard.readline().decode('utf-8')
        # print(line, end='')
        # time.sleep(READ_SERIAL_DELAY)

if __name__ == '__main__':
    main()
    