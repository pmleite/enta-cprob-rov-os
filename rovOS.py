#!/usr/bin/env python3
import serial
import time
import pyshine as ps 
import cv2

HTML="""
html><head><title>ROV</title>
</head>
<body>
<h1>ROV</h1>
<img src="stream.mjpg" width="640" height="480" autoplay playsinline/>
</body>
</html>
"""

def main():
    
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,HTML)
    address = ('192.168.1.222',9000)
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture('myCampture.mp4')
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        capture.set(cv2.CAP_PROP_FPS,30)
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        StreamProps.set_Capture(StreamProps,capture)
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        print("Server started at "+str(address))
        server.serve_forever()
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()
        
        
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
    


    
