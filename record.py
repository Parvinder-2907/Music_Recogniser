import pyaudio
import wave
'''******************************************************************'''

RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
FORMAT = pyaudio.paInt16
CHANNELS = 2
WAVE_OUTPUT_FILENAME = "hello.wav"
audio = pyaudio.PyAudio()


 '''+++++++++++++++++++++++++++START RECORDING++++++++++++++++++++++++'''


stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

print ("recording sample...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
'''+++++++++++++++++++++++++++++STOP RECORDING++++++++++++++++++++++++++'''


stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()


'''*******************************************************************************************'''