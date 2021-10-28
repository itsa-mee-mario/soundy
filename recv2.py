import numpy as np
from time import sleep as wait
import sounddevice as sd
import serial
ser1 = serial.Serial("/dev/ttyACM0", 9600)
prev, now = 0,0

def audio_callback(indata, frames, time, status, now=0):

   volume_norm = np.linalg.norm(indata) * 10
   wait(0.06)
   prev = now
   now = int(volume_norm)
   if prev>now:
   	print("dec")
   	ser1.write("d".encode())
   	
   if now>prev:
   	print("inc")
   	ser1.write("i".encode())
   	
   	
   	

   	

stream = sd.InputStream(callback=audio_callback, samplerate=2000)
with stream:
   while True: 
   	sd.sleep(1)
   	
   	

   
