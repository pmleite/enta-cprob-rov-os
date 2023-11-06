# enta-cpro-rov-os

Firmware do ROV

RaspberyPi Version:
Linux raspberrypi 6.1.61-v8+ #1696 SMP PREEMPT Thu Nov  2 16:44:46 GMT 2023 aarch64 GNU/Linux

## Prerequisitos

Algumas operações devem ser executadas no RaspberyPI antes de arrancar com os componentes de software.

### Ativar deteção de câmara

Editar o ficheiro de boot config.txt

```bash
sudo nano /boot/config.txt 
```

Verificar se as entradas das variaveis estão de acordo com o seguinte:

```bash
#start_x=1            #(Se existir, comentar)
camera_auto_detect=1  #(Se não existir, criar)

[all]
gpu_mem=256           #(Se não existir, criar)
dtoverlay=w1-gpio     #(Se não existir, criar)
enable_uart=1         #(Se não existir, criar)
```

### Ativar o serviço de VNC Server

```bash
sudo /etc/vnc/vncservice start vncserver-x11-serviced
```

### Arrancar com o rovOS

```bash
runrov
```

## Aceder ao stream de video

Para aceder ao stream de video deve utilizar o VLC, criar uma configuração de "Network Stream" com as seguintes propriedades.

```config
tcp/h264://192.168.1.31:8888
```
