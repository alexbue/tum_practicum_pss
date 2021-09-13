#!/usr/bin/env python
# coding: utf-8

# ## 1.3 Audio direkt in das Jupyter Notebook aufnehmen
# 
# An dieser Stelle ist es wichtig vorab in den Einstellungen des Betriebssystems den 
# korrekten Sound-Eingang vom Soundinterface für das Mikrofon als Standard eingestellt zu haben.
# Das Jupyter Notebook wird immer nur auf das eingestellte Standard-Mikrofon zugreifen. 
# Je nach Browser muss hier zusätzlich dem Mikrofon-Einsatz zugestimmt werden.
# 
# <img src="aassets/mikrofon_browser.png" width="400" /></br>
# 
# test
# </br>
# test
# test
# test
# ### Benötigte Packages

# In[1]:


import numpy as np # for faster operations with floating point numbers
#import soundfile as sf  # for writing/reading soundfiles
from IPython.display import Audio # audio player
from IPython.core.display import display # enable visual integration of audio player
import matplotlib.pyplot as plt # plotting visuals
from ipywebrtc import AudioRecorder, CameraStream # enable multimedia-streaming into to the juypter-notebook
import scipy
from scipy import signal  # signal processing


# ### Aufnahme mit dem AudioRecorder
# Nach Ausführung der folgenden Zelle erscheint der Audio-Recorder mit einem Aufnahme-Button und einem Speichern-Symbol. </br>
# Die aufgenommene Audio-Datei wird automatisch lokal als 'recording.webm' gespeichert und kann nach Abschluss der Aufnahme direkt angehört werden.

# In[2]:


camera = CameraStream(constraints={'audio': True,'video':False})
recorder = AudioRecorder(stream=camera)
print("\n", "Audio-Recorder", "\n") # print info
recorder


# ### Konvertierung unserer Aufnahme von .webm zu .wav
# Der verwendete Multimedia-Recorder speichert automatisch aufgenommenes Audio im .webm-Dateiformat, einem modernen Multimedia-Format. Wir könnten das zwar auch im Weiteren verwenden, </br>
# möchten aber klassischerweise unsere Audio-Datei als .wav speichern. Dazu konvertieren wir die eben aufgenommene Datei ('recording.webm') mit Hilfe des ffmpeg-packages. </br> Hinweis: Code-Ausführungen mit einem ! am Anfang sind Shell-Befehle, wie sie auch im Terminal oder der Konsole benutzt werden. Diese können genauso direkt im Jupyter Notebook ausgeführt werden, wie Python Code.

# In[3]:


with open('recording.webm', 'wb') as f: #convert .webm to .wav with ffmpeg
    f.write(recorder.audio.value)
get_ipython().system("ffmpeg -i recording.webm -ac 1 -f wav 'files/recording.wav' -y -hide_banner -loglevel panic")


# ### Meta-Daten auslesen
# Um zu Testen ob beim Konvertieren und Speichern alles geklappt hat, können wir uns die Meta-Daten auslesen lassen. 

# In[4]:


get_ipython().system('sndfile-info files/recording.wav')


# ### Erneutes Laden unserer konvertierten Aufnahme
# Zur weiteren Analyse und Verarbeitung laden wir unsere konvertierte und gespeicherte Aufnahme als .wav nochmal: 

# In[5]:


audio_signal, samplerate = sf.read('files/recording.wav') # load recorded sound again as a (numeric) NumPy array


# ### Anhören des aufgenommenen Signals
# Natürlich können wir auch direkt nochmal testen, wie sich unser rohes Audiosignal als .wav anhört.

# In[15]:


display(Audio(audio_signal, rate=samplerate)) # add audioplayer to play the sound


# ### Digitale Darstellung
# Wir können uns das digitale Signal, so wie es vom Computer repräsentiert wird, auch ansehen - als numerisches Array. Die Anzahl der Samples ist dabei evtl zu groß, als dass das Array vollständig dargestellt werden kann und nur Anfang und Ende des Arrays in der Ausgabe gezeigt werden.

# In[16]:


print("\n", audio_signal, "\n") # show the audio-signal numerically - as it is stored and used for processing and analysis


# ### Plotten des Audio-Signals
# Für eine etwas intuitivere Darstellung können wir unser Signal auch wieder plotten und damit zur weiteren Analyse etwas greifbarer machen.

# In[17]:


plt.plot(audio_signal) # plot the audio-signal
plt.grid(True)
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.show()


# </br>
# 
# ## 2.2 Zusammenfassung
# ### Audio-Recording
# Nochmal alle Einzelschritte zur Aufnahme, Konvertierung, Anzeige und Abspielen unserer Signals zusammengefasst und zwei Zellen ausgeführt. Die erste Zelle muss zuerst alleine für die Aufnahme seperat ausgeführt werden, danach erledigt die zweite alle Analysen und Ausgaben zu der Aufnahme.

# In[10]:


import numpy as np # for faster operations with floating point numbers
import soundfile as sf  # for writing/reading soundfiles
from IPython.display import Audio # audio player
from IPython.core.display import display # enable visual integration of audio player
import matplotlib.pyplot as plt # plotting visuals
from ipywebrtc import AudioRecorder, CameraStream # enable multimedia-streaming into to the juypter-notebook

camera = CameraStream(constraints={'audio': True,'video':False})
recorder = AudioRecorder(stream=camera)
print("\nAudio-Recorder:") # print info
recorder


# In[11]:


with open('recording.webm', 'wb') as f: #convert .webm to .wav with ffmpeg
    f.write(recorder.audio.value)
get_ipython().system("ffmpeg -i recording.webm -ac 1 -f wav 'files/recording.wav' -y -hide_banner -loglevel panic")

get_ipython().system('sndfile-info files/recording.wav # check meta-data')

audio_signal, samplerate = sf.read('files/recording.wav') # load recorded sound again as a (numeric) NumPy array

plt.plot(audio_signal) # plot the audio-signal
plt.grid(True) # turn on grid 
plt.xlabel("Time [samples]") # title of the x-axis
plt.ylabel("Amplitude") # title of the y-axis
plt.show() # show the plot

print("\n", audio_signal, "\n") # show the audio-signal numerically - as it is stored and used for processing and analysis

display(Audio(audio_signal, rate=samplerate)) # add audioplayer to play the sound


# </br></br>
# 
# [zurück: 1.2 Schreiben von Audio-Dateien](1_2_Schreiben.ipynb) | [vor: 2.1 Signalerzeugung](2_1_Signalerzeugung.ipynb)
