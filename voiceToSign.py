import speech_recognition as sr
from PIL import Image
import imageio.v2
import imageio

import matplotlib.pyplot as plt
import os
import skvideo.io
import numpy as np
from matplotlib.animation import FuncAnimation
import tkinter as tk
import imageio
from tkinter import messagebox

r = sr.Recognizer()
Mytext = ""



try:
    
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recognizing...")
        audio_data = r.record(source,5)
    
        # convert speech to text
        Mytext = r.recognize_google(audio_data)
        Mytext = Mytext.lower()
        print(Mytext)

except:
    print("Failed to Recognise, pls try again")

def display(img,title="Original"):
        plt.imshow(img,cmap='gray'),plt.title(title)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(2)
        plt.close


if(Mytext != ""):
    for l in Mytext:
        if l == ' ':
            l = '_'
            
        img=imageio.v2.imread("SLD/"+l+'.jpg')
        display(img,l)
        
