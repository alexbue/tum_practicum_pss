#!/usr/bin/env python
# coding: utf-8

# # 1.2 Speichern von Audio-Dateien
# 
# ## Benötigte Packages
# Wir verwenden auch zum Schreiben von Sounddateien das [pysoundfile](http://github.com/bastibe/SoundFile) package. Dokumentation auf http://pysoundfile.readthedocs.org

# In[1]:


import numpy as np # for faster operations with floating point numbers
import soundfile as sf  # for writing/reading soundfiles
import librosa as lr # for writing/reading soundfiles


# Audio-Daten zu speichern ist genauso einfach wie sie zu lesen. Dazu benutzen wir die Funktion [sf.write()](http://pysoundfile.readthedocs.org/#soundfile.write):

# In[2]:


audio_signal, samplerate = sf.read('files/file.wav')
sf.write('files/audio_file_16bit_fixed.wav', audio_signal, samplerate)


# ### Meta-Daten auslesen
# Um zu Testen ob beim Konvertieren und Speichern alles geklappt hat, können wir uns die Meta-Daten auslesen lassen. 

# In[3]:


get_ipython().system('sndfile-info files/audio_file_16bit_fixed.wav')


# ### Präzision / Subtypes
# 
# #### 16-bit Festkommazahlen (fixed points)
# Standardmäßig werden die .wav Dateien als 16-bit Festkommazahlen (a.k.a. `'PCM_16'`) geschrieben.
# Die jeweiligen Standardeinstellung für jedes Dateiformat lassen sich hier nachschlagen [sf.default_subtype()](http://pysoundfile.readthedocs.org/#soundfile.default_subtype). </br>
# 
# Wir können den Standard-Subtype für die unterschiedlichen Dateiformate (hier 'WAV') auch direkt im Code überprüfen:

# In[4]:


sf.default_subtype('WAV')


# #### Verwendung von anderen Subtypes
# 
# Wenn wir unsere Audio-Dateien mit einer grösseren Präzision (numerischer Genauigkeit) speichern wollen, können wir sie zum Beispiel auch als 32-bit-Fliesskommazahlen ('FLOAT') speichern. 

# In[5]:


sf.write('files/audio_file_32bit_float.wav', audio_signal, samplerate, subtype='FLOAT')


# #### Überprüfung 
# Überprüfen wir kurz, ob das funktioniert hat und lesen dazu nochmal die Metadaten aus:

# In[6]:


get_ipython().system('sndfile-info audio_file_32bit_float.wav')


# In der letzten Ausgabe sehen wir unter 'Format', dass die Audio-Datei korrekt mit Fliesskommazahlen ('IEEE_FLOAT') und mit Bit-Größe ('Bit Width') 32-bit gespeichert wurde.
# 
# #### Alle möglichen Subtypes
# 
# Wir können uns alle möglichen Subtypes der jeweiligen Dateiformate (hier im Beispiel 'WAV') ausgeben lassen, mit denen wir explizit die numerische Genauigkeit und damit auch die Qualität unserer gespeicherten Audio-Daten bestimmen können:

# In[7]:


sf.available_subtypes('WAV')


# </br></br>
# [zurück: 1.1 Lesen von Audio-Dateien](1_1_Lesen.ipynb) | [vor: 1.3 Audio direkt in das Jupyter Notebook aufnehmen](1_3_Recording.ipynb)

# In[ ]:




