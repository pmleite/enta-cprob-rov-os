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
pip3 install pyshine==0.0.9
