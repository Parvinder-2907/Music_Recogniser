from scipy.fftpack import fft
from scipy.io import wavfile
from math import log


'''*******************************************************************************************************'''

class library(object):


     def __init__(self, name, frequency, size):
         self.name = name
         self.frequency = frequency
         self.winsize = size
         self.db = {}

'''*******************************************************************************************************'''

     def get_index(self, value, line):
         for q in range(len(line)):
            if line[q][0] <= value and line[q][1] >= value:
                 return q

'''*******************************************************************************************************'''

    def add_track(self, track, name):
         iterations = len(track)//self.winsize
         for i in range(iterations):
             if int((i+1)*self.winsize) > len(track):
                 chunk = fft(track[int((i)*self.winsize) : len(track)])
                 chunk = chunk[0:len(chunk)//2]
             else:
                 chunk = fft(track[int((i)*self.winsize) : int((i+1)*self.winsize)])
                 chunk = chunk[0:len(chunk)//2]

             tf = getfourpoints(chunk, self.frequency)
             tag = hash(sum(tf))
             self.db[tag] = [i, name]
         print("done")

'''*******************************************************************************************************'''

     def getfourpoints(self, sample, line):
         rslt = [0,0,0,0]
         for frq in sample:
             index = get_index(frq, line)
             value = log(abs(frq) + 1)
             if index is not None and rslt[index] < value:
                  rslt[index] = round(value, 0)
         return rslt
     
     

'''*******************************************************************************************************'''








