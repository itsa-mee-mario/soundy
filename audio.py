import pyaudio
import wave
import audioop
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pyfirmata



CHUNK = 64
FORMAT = pyaudio.paInt16
CHANNELS = 1


p = pyaudio.PyAudio()



stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate = 1000,
                input=True,
                frames_per_buffer=CHUNK,
                )


stream.start_stream()

while True:
    data = stream.read(CHUNK)
    rms = audioop.rms(data, 2)    # here's where you calculate the volume

    print(rms)

   
p.terminate()
