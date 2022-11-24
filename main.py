import tkinter as tk
from tkinter import *
from tkinter import Canvas
from tkinter.ttk import *
from PIL import Image, ImageTk


window_1 = tk.Tk()


#window backend

ico = Image.open('icon.jpg')
photo = ImageTk.PhotoImage(ico)
window_1.wm_iconphoto(False, photo)
window_1.resizable(0, 0)
window_1.geometry('350x350')
window_1.title('Dragoman')

#window frontend

#GIF in my_image variable
#Give the entire file address along with the file name and gif extension
#Use \\ in the address
#The image given by me is C:\\UserAdmin\\Device\\Desktop2\\canyon.gif
frameCnt = 40
frames = [PhotoImage(file='gif1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]


def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window_1.after(10, update, ind)
    
label = Label(window_1)
label.pack()
window_1.after(0, update, 0)

#window_1.mainloop()
