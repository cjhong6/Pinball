# # Tkinter is a built-in python package. It is used for creating GUI application.
# # Tkinter is cross-platform so it can run in windows and linux system
# # Use Tkinter's canvas to create a Pinball game
import random
import time
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3


# Communicate with the window manager
tk = tkinter.Tk()
tk.title("Pinball") #Set window title
tk.resizable(0,0) #The width flag controls whether the window can be resized horizontally by the user.(0,0) means can't be resize
tk.wm_attributes("-topmost", 1) #this window is always placed on top of other windows
canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg="powderblue") #create a canvas, bd=borderwidth
canvas.pack() #organizes widgets in blocks before placing them in the parent widget
tk.mainloop() #call mainloop when the application is ready to run
