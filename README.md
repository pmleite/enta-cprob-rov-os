# enta-cpro-rov-os #

Firmware do ROV

# Configuring and test RaspberyPy CAM #

run:

```
sudo rasp-config
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
