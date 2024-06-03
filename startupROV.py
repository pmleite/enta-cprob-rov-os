import subprocess, time

def main():
  
    # Start video stream sub-process
    try:
      subprocess.Popen(["python3", "videoStream.py"])
      print("Video Stream up...!")
      time.sleep(5)  
    except:
      print("Erro ao iniciar o video stream.")
      print("Verifique o compoenente libcamera-vid e tente novamente")
        
      
    # Start main system sub-process  
    try:
      subprocess.Popen(["python3", "enta-cprob-rov-os.py"])
      print("Main system up...!") 
      time.sleep(3)     
    except:
      print("Erro ao iniciar o sistema principal.")
      print("Verifique o compoenente enta-cprob-rov-os.py e tente novamente")
      exit()   
    
if __name__ == '__main__':
    main()
