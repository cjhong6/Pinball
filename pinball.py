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
class Ball:
    def __init__(self,x,y,canvas,board,color):
        self.canvas = canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,x,y) #put the ball on canvas
        self.board = board

        # Random selected X and Y direction to move
        starts = [-4,-5,-6,4,5,6]
        random.shuffle(starts)
        self.xDirection=starts[0]
        self.yDirection=-3

        self.height=self.canvas.winfo_height()
        self.width=self.canvas.winfo_width()

        self.hit_bottom=False
        time.sleep(3)
    def draw(self):

        self.canvas.move(self.id,self.xDirection,self.yDirection)
        pos=self.canvas.coords(self.id)

        # ball reflect after hit the board
        if self.hit_board(pos) == True:
            self.yDirection = -5

        if(pos[1]<=0):
            self.yDirection=5
        if(pos[3]>=self.height):
            self.yDirection=-5
        if(pos[0]<=0):
            self.xDirection=5
        if(pos[2]>=self.width):
            self.xDirection=-5

        if pos[3] >= self.height:
            self.hit_bottom=True

    def hit_board(self,pos):
        board_pos = self.canvas.coords(self.board.id)
        if pos[2]>=board_pos[0] and pos[0]<=board_pos[2]:
            if pos[3]<=board_pos[3] and pos[3]>=board_pos[1]:
                return True
        return False

class Board:
    def __init__(self,canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,150,10,fill=color)
        self.canvas.move(self.id,200,350)
        self.xDirection=0
        self.width=self.canvas.winfo_width()
        # bind the event listening based on the keyborad key
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def draw(self):
        self.canvas.move(self.id,self.xDirection,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.xDirection=0
        if pos[2]>=self.width:
            self.xDirection=0

    def move_left(self,evt):
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.xDirection=0
        else:
            self.xDirection=-5
    def move_right(self,evt):
        pos=self.canvas.coords(self.id)
        if pos[2]>=self.width:
            self.xDirection=0
        else:
            self.xDirection=5


board=Board(canvas,'#C19A6B')
ball=Ball(250,200,canvas,board,'#ff546e')

while True:
    if ball.hit_bottom == False:
        ball.draw()
        board.draw()
    else:
        tk.destroy()
    tk.update()
    time.sleep(0.01)
