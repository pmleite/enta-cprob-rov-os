import subprocess

def main():
    
    try:
        subprocess.Popen(["python3", "videoStreamAndControls"])
        print("Video Stream iniciado com sucesso!")
    except:
        print("Erro ao iniciar o video stream.")
        print("Verifique o compoenente libcamera-vid e tente novamente")

    
if __name__ == '__main__':
    main()
    