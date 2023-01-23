from pytube import YouTube
from tkinter import*
from tkinter import messagebox, filedialog
 
'''link = input("Enter link: ")
Download(link)'''

root = Tk()
root.geometry("600x500")
#root.resizable(0, 0)
root.title("LEKU's Downloader")

Label(root, text="Youtube video downloader", font="arial 20 bold").pack()
link = StringVar()

Label(root, text="Paste link here: ", font="arial 15 bold").place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def Download():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = "Video Downloaded", font="arial 15").place(x=180, y=210)


Button(root, text="Download", font="san-serif 15 bold", bg="cyan", padx=2, command=Download).place(x=212, y=150)
root.mainloop()