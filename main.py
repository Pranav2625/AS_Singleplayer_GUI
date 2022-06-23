from tkinter import *
from functools import partial


class Single_Game:
  def __init__(self, partner):

    self.single_frame = Frame(width = 700, height = 500, bg = "Green") # Window Frame
    self.single_frame.grid()

    self.dealer_side = Label(self.single_frame, text = "Dealer", font = "Times 14 bold", # Dealer's side
                              bg = '#733f19', fg = "White", padx = 330, pady = 12) 
    self.dealer_side.place(x = -10, y = 0) # used place to postion the strip

    starting_credit = 500
    starting_bet = 0

    self.start_cred_display = Label(self.single_frame, text = ("Credits: ", starting_credit), font = "Times 10", bg = 'orange')
    self.start_cred_display.place(x = 580, y = 80)


if __name__ == "__main__":
  root = Tk()
  root.title("Single Player Mode")
  screen = Single_Game(root)
  root.mainloop()