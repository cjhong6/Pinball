# # Tkinter is a built-in python package. It is used for creating GUI application.
# # Tkinter is cross-platform so it can run in windows and linux system
# # Use Tkinter's canvas to create a Pinball game
import random
import time
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3

# Communicate with the window manager
tk = tkinter.Tk() #create TK window
tk.title("Pinball") #Set window title
tk.resizable(0,0) #The width flag controls whether the window can be resized horizontally by the user.(0,0) means can't be resize
tk.wm_attributes("-topmost", 1) #this window is always placed on top of other windows
canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg="powderblue") #create a canvas, bd=borderwidth
canvas.pack() #put the canvas(widget) to the tk window
tk.update() #Update the window size

#create pinball object
class Ball():
    def __init__(self,x,y,canvas,color):
        self.canvas = canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,x,y) #put the ball on canvas

        # Random selected X and Y direction to move
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.xSpeed=starts[0]
        self.ySpeed=starts[1]

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_weight = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.xSpeed,self.ySpeed)
        pos = self.canvas.coords(self.id)
        if(pos[1]<=0):
            self.ySpeed = 1
        if(pos[3]>=self.canvas_height):
            self.ySpeed = -1
        if(pos[0]<=0):
            self.xSpeed = 1
        if(pos[2]>=self.canvas_weight):
            self.xSpeed = -1

class Board:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.id=canvas.create_rectangle(0,0,150,10,fill=color)
        self.canvas.move(self.id,200,350)

    def draw(self):
        pass

ball = Ball(250,200,canvas,'#ff546e')
board = Board(canvas,'#C19A6B')

while True:
    ball.draw()
    board.draw()
    tk.update()
    time.sleep(0.01)
