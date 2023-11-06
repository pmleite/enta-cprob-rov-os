# enta-cpro-rov-os #
Firmware do ROV

# Prerequisitos


sudo nano /boot/config.txt

#start_x=1
camera_auto_detect=1

[all]
gpu_mem=256
dtoverlay=w1-gpio
enable_uart=1


RaspberyPi Version:
Linux raspberrypi 6.1.61-v8+ #1696 SMP PREEMPT Thu Nov  2 16:44:46 GMT 2023 aarch64 GNU/Linux

sudo /etc/vnc/vncservice start vncserver-x11-serviced


Docker (into raspberyPI)
```
sudo apt-get update
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

# Stream server

```
docker run -d --restart=always --name restreamer \
   -v /opt/restreamer/config:/core/config -v /opt/restreamer/data:/core/data \
   --privileged \
   -p 8080:8080 -p 8181:8181 \
   -p 1935:1935 -p 1936:1936 \
   -p 6000:6000/udp \
   datarhei/restreamer:rpi-latest
```


docker run -d --name restreamer \
   -v /opt/restreamer/config:/core/config -v /opt/restreamer/data:/core/data \
   --privileged \
   -p 8080:8080 -p 8181:8181 \
   -p 1935:1935 -p 1936:1936 \
   -p 6000:6000/udp \
   datarhei/restreamer:rpi-latest

Se obtiver um erro de acesso ao docker.sock, execute:

```
sudo chmod 666 /var/run/docker.sock
```
























# Configuring and test RaspberyPy CAM #

Atenção falta barra via VNC
https://raspberrypi.stackexchange.com/questions/122579/after-fresh-install-of-raspberry-os-the-menu-bar-is-missing-in-tightvnc-session



run:

```
sudo raspi-config
```

Go to interface options and activate camera interface

To teste life video run:

```
raspivid -t 0
```

Start straming type
```
raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264
```

# dependencias
sudo apt install autoconf automake build-essential pkgconf libtool git libzip-dev libjpeg-dev gettext libmicrohttpd-dev libavformat-dev libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev default-libmysqlclient-dev libpq-dev libsqlite3-dev libwebp-dev


sudo wget https://github.com/Motion-Project/motion/releases/download/release-4.5.1/$(lsb_release -cs)_motion_4.5.1-1_$(dpkg --print-architecture
).deb

sudo dpkg -i $(lsb_release -cs)_motion_4.5.1-1_$(dpkg --print-architecture).deb











pip3 install pyshine==0.0.9





Local PC
pip3 install opencv-python

RaspberiPi4
sudo apt-get install libopencv-dev python3-opencv
