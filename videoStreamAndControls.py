# app.py
from flask import Flask, render_template, Response, request
import cv2
import pigpio

tcp_port = 5000

app = Flask(__name__)
pi = pigpio.pi()

# Video capture
camera = cv2.VideoCapture(0)

def gen():
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Video streaming
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Motor control function
def set_motor_speed(motor, speed):
    pwm_value = int((speed + 100) * 2.55)
    pi.set_PWM_dutycycle(motor, pwm_value)
    
@app.route('/control', methods=['POST'])
def control():
    motor = int(request.form['motor'])
    speed = int(request.form['speed'])
    set_motor_speed(motor, speed)
    return '', 204
  
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=tcp_port)