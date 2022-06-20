from tkinter import *
from functools import partial


class Single_Game:
  def __init__(self, partner):

    self.single_frame = Frame(width = 900, height = 500, bg = "Green")
    self.single_frame.grid()



if __name__ == "__main__":
  root = Tk()
  root.title("Single Player Mode")
  screen = Single_Game(root)
  root.mainloop()