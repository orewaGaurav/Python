# Sound Recorder Task from CIPHERBYTE
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import wavio as wv
from tkinter import *
root=Tk()
root.geometry("1000x600")
root.config(bg='black')
root.title("Voice Recorder")
label0=Label(root,text="                 ",font=("arial",25),bg='black',fg='white')
label0.grid(row=0,column=0)
label1=Label(root,text="This is a task from CipherByte",font=("arial",25),bg='black',fg='white')
label1.grid(row=0,column=1)
def play():
    file='rec.wav'
    data , fs = sf.read(file)
    sd.play(data,fs)
    sd.wait()
def close():
    exit()
def start():
    emptyline=Label(root,text="                 ",font=("arial",25),bg='black',fg='white')
    emptyline.grid(row=5,column=1)
    recordinglabel=Label(root,text="Recording started",font=("arial",25),bg='black',fg='white')
    recordinglabel.grid(row=6,column=1)
    dur=float(duration.get())
    freq = 48000 
    recording=sd.rec(int(dur*freq),samplerate=freq,channels=2)
    sd.wait()
    write("rec.wav",freq,recording)
    recordinglabel=Label(root,text="Recording Saved..",font=("arial",25),bg='black',fg='white')
    recordinglabel.grid(row=6,column=1)
    playbutton=Button(root,text="Play Recording",command=play,font=("arial",30),bg='black',fg='white')
    playbutton.grid(row=7,column=2)
emptyline=Label(root,text="                 ",font=("arial",25),bg='black',fg='white')
emptyline.grid(row=1,column=1)
durationlabel=Label(root,text="Duration in sec",font=("arial",25),bg='black',fg='white')
durationlabel.grid(row=2,column=0)
duration=Entry(root,font=("arial",25),bg='black',fg='white')
duration.grid(row=2,column=1)
emptyline=Label(root,text="                 ",font=("arial",25),bg='black',fg='white')
emptyline.grid(row=3,column=1)
startbutton=Button(root,text="Start Recording",command=start,font=("arial",30),bg='black',fg='white')
startbutton.grid(row=4,column=1)
closebutton=Button(root,text="Close",command=close,font=("arial",30),bg='black',fg='white')
closebutton.grid(row=8,column=2)
root.mainloop()