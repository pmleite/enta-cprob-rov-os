#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()


# import serial
# import time
# import pyshine as ps 
# import cv2

# IP_ADDRESS      = '192.168.1.222'
# UDP_STREAM_PORT = 9000

# HTML="""
# html><head><title>ROV</title>
# </head>
# <body>
# <h1>ROV</h1>
# <img src="stream.mjpg" width="640" height="480" autoplay playsinline/>
# </body>
# </html>
# """

# def main():
    
#     StreamProps = ps.StreamProps
#     StreamProps.set_Page(StreamProps,HTML)
#     address = (IP_ADDRESS,UDP_STREAM_PORT)
#     try:
#         StreamProps.set_Mode(StreamProps,'cv2')
#         capture = cv2.VideoCapture('myCampture.mp4')
#         capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
#         capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
#         capture.set(cv2.CAP_PROP_FPS,30)
#         capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
#         StreamProps.set_Capture(StreamProps,capture)
#         StreamProps.set_Quality(StreamProps,90)
#         server = ps.Streamer(address,StreamProps)
#         print("Server started at "+str(address))
#         server.serve_forever()
#     except KeyboardInterrupt:
#         capture.release()
#         server.socket.close()
        
    
# if __name__ == '__main__':
#     main()
    


    
