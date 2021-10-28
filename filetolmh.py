from scipy.io.wavfile import read
import pygame, sys, time
from numpy import fft
import serial
ser1 = serial.Serial("/dev/ttyACM0", 115200)

import os


file_name = "audio.wav"
os.system("mpg123 " + file_name)
frame_rate, amplitude = read(file_name)
frame_skip = 10
amplitude = amplitude[:,0] + amplitude[:,1]
amplitude = amplitude[::frame_skip]
frequency = list(abs(fft.fft(amplitude))/100000)
pygame.init()


now = time.time()	

for i in range(len(amplitude)):
   
   print(int(frequency[i]))
   
   if int(frequency[i]) < 10 and int(frequency[i])>2 :
   	print("low")
   	ser1.write("dl".encode())
   	
   if (int(frequency[i]) > 10 and int(frequency[i]) < 20):
   	print("med")
   	ser1.write("dm".encode())
	
   if int(frequency[i]) >20:
   	print("oof")
   	ser1.write("dh".encode())
   	

  
