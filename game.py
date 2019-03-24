from tkinter import *
import time

root = Tk()
root.title("Bounce")
root.resizable(0, 0)

canvas = Canvas(root, width=500, height=500, bg="black")
canvas.pack()

class Ball:

    def __init__(self, canvas, color, speed):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 247)
        self.x = -speed
        self.y = -speed
        self.speed = speed
        self.hit_bottom = False
        self.count = 0

    def hit_paddle(self, paddle):
        pos_paddle = canvas.coords(paddle.id)
        pos_ball = self.canvas.coords(self.id)

        if pos_ball[2] >= pos_paddle[0] and pos_ball[0] <= pos_paddle[2]:
            if pos_ball[3] == pos_paddle[1]:
                self.y = -self.speed
                a = canvas.create_text(245, 50, text=self.count, fill="white")
                canvas.itemconfig(a, fill="black")
                self.count = self.count + 1
                a = canvas.create_text(245, 50, text=self.count, fill="white")


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = self.speed
        if pos[3] >= 500:
            self.hit_bottom = True
            canvas.create_text(245,100, text="Game Over", fill="white")
        if pos[0] <= 0:
            self.x = self.speed
        if pos[2] >= canvas.winfo_width():
            self.x = -self.speed


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 80, 10, fill=color)
        self.canvas.move(self.id, 240, 480)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def right(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[2] >= self.canvas.winfo_width():
            self.x = 0
        else:
            self.x = 2

    def left(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        else:
            self.x = -2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas.winfo_width():
            self.x = 0


ball = Ball(canvas, "red", 2)
paddle = Paddle(canvas, "blue")


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        ball.hit_paddle(paddle)
    root.update()
    time.sleep(0.01)

root.mainloop()