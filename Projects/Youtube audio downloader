import tkinter as tk
from tkinter import Canvas
from pytube import YouTube

def Download_Audio():
    url = YouTube(str(link.get()))
    print(url.streams.get_highest_resolution().resolution)
    print(url.title)
    print(url.author)
    print(url.length)
    tk.Label(window, text=url.title, font='Times 12', fg="white", bg="#2B2B2B").place(x=54,y=245)
    tk.Label(window, text="Author:   " + url.author, font='Times 12', fg="white", bg="#2B2B2B").place(x=54, y=270)
    audioStream = url.streams.filter(type="audio")
    print(audioStream.first())
    audioStream.first().download("audios/")
    tk.Label(window, text='Download Complete!', font='Times 16', fg="White", bg="#2B2B2B").place(x=188, y=102)


window = tk.Tk()
window.geometry("600x400")
window.config(bg="#2B2B2B")
window.resizable(width=False, height=False)
window.title('!AUDIOFY!')
link = tk.StringVar()
tk.Label(window, text='AUDIOFY AUDIO DOWNLOADER', font='Times 16 bold',
         fg="White", bg="#2B2B2B").place(x=124, y=14)
tk.Label(window, text='Paste video link:', font='Times 16', fg="White",bg="#2B2B2B").place(x=54, y=148)
link_enter = tk.Entry(window,width=55, textvariable=link, font='Times 12', bg="#F07401").place(x=58, y=180)
tk.Button(window, text='EXTRACT AUDIO', font='Times 14', fg="Black", bg='#F07401', padx=2,
          command=Download_Audio).place(x=210, y=337)
window.mainloop()
