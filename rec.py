import numpy as np
from time import sleep as wait
import sounddevice as sd
import serial
ser1 = serial.Serial("/dev/ttyACM0", 115200)
wait(1)
ser1.write("d".encode())


def audio_callback(indata, frames, time, status):
   volume_norm = np.linalg.norm(indata) * 10
 
  

   wait(0.001)
   if int(volume_norm) < 10 and int(volume_norm)>2 :
   	print("low")
   	ser1.write("d".encode())
   	
   if (int(volume_norm) > 10 and int(volume_norm) < 20):
   	print("med")
   	ser1.write("dm".encode())
	
   if int(volume_norm) >20:
   	print("oof")
   	ser1.write("dh".encode())
   	
   
   	

stream = sd.InputStream(callback=audio_callback)
with stream:
   while True: 
   	sd.sleep(1)
   	
   	
   	

   
