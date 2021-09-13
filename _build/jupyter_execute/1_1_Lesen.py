#!/usr/bin/env python
# coding: utf-8

# ## 1.1 Lesen von Audio-Dateien
# 
# ### Benötigte Packages
# Wir verwenden zum Lesen und Schreiben von Sounddateien das [pysoundfile](http://github.com/bastibe/SoundFile) package. Dokumentation auf http://pysoundfile.readthedocs.org

# In[1]:


import numpy as np # for faster operations with floating point numbers
#import librosa as lr # for reading/writing audio files
import soundfile as sf # for reading/writing audio files
from IPython.display import Audio # audio player
from IPython.core.display import display # enable visual integration of audio player
import matplotlib.pyplot as plt # for plotting visuals


# ### Audio-Datei einlesen
# 
# Um eine lokal abliegende Audio-Datei einzulesen, verwenden wir die Funktion sf.read(). Die Funktion gibt als Ausgabe, das eigentliche Signal, als auch dessen Samplerate zurück.

# In[2]:


#audio_signal, samplerate = sf.read('files/file.wav') # read audio file
audio_signal, samplerate = sf.read('files/file.wav')


# ### Anhören der eingelesenen Audio-Datei
# Natürlich können wir auch direkt testen, wie sich unser eingelesenes Audiosignal als anhört:

# In[3]:


display(Audio(audio_signal, rate=samplerate)) # display audioplayer with loaded audio-signal


# ### Digitale Darstellung
# 
# Wir können uns das digitale Signal, so wie es vom Computer repräsentiert wird, auch ansehen - als numerisches Array. Die Anzahl der Samples ist dabei evtl zu groß, als dass das Array vollständig dargestellt werden kann und nur Anfang und Ende des Arrays in der Ausgabe gezeigt werden.

# In[4]:


print(audio_signal) # show impulse-signal in its numeric representation 


# ### Plotten des Audio-Signals
# Für eine verständlichere und intuitivere Darstellung können wir uns das Audio-Signal auch plotten:

# In[5]:


plt.plot(audio_signal); # plot the audio-signal
plt.grid(True)
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.show()


# ### Samples auslesen
# 
# Wenn wir uns die Anzahl der Samples ausgeben lassen möchten, geht das auch ganz einfach:

# In[6]:


print(audio_signal.shape)


# ### Samplerate prüfen
# 
# Überprüfen wir kurz die Samplerate der eingelesenen Audio-Datei.

# In[7]:


print(samplerate)


# ### Meta-Daten auslesen
# Grundsätzlich können wir auch jederzeit die Meta-Daten der lokalen Audio-Datei abgreifen und so detaillierte Informationen über die Datei auf einen Schlag bekommen: 

# In[8]:


get_ipython().system('sndfile-info files/file.wav')


# </br>
# 
# ## 1.2 Zusammenfassung
# ### Audio-Daten einlesen
# Nochmal alle Einzelschritte zum Einlesen, Abspielen und Anzeigen des Audio-Signals aus einer Audio-Datei zusammengefasst und in einer Zelle ausgeführt:

# In[9]:


import numpy as np # for faster operations with floating point numbers
import soundfile as sf # for writing/reading audio files
from IPython.display import Audio # audio player
from IPython.core.display import display # enable visual integration of audio player
import matplotlib.pyplot as plt # plotting visuals

audio_signal, samplerate = sf.read('files/file.wav') # read audio file and its samplerate

get_ipython().system('sndfile-info files/file.wav # print meta-data')

plt.plot(audio_signal) # plot the audio-signal
plt.grid(True) # turn on grid 
plt.xlabel("Time [samples]") # title of the x-axis
plt.ylabel("Amplitude") # title of the y-axis
plt.show() # show the plot

print("\n", audio_signal, "\n") # show impulse-signal in its numeric representation 
display(Audio(audio_signal, rate=samplerate)) # add audioplayer to play the sound

