from tkinter import *
from functools import partial
import random

card_num_1 = random.randint(1, 5)
card_num_2 = random.randint(1, 5) 

root = Tk()
root.title("Single Player Mode") # Window title

sngle_frame = Frame(root, width=700, height=500, bg="green")  # Window Frame
sngle_frame.grid()

dealer_side = Label(sngle_frame, text="Dealer", font="Times 14 bold", # Dealer's Side
                    bg="#733f19", fg="white", padx=330, pady=12)      # of the table
dealer_side.place(x=-10, y=0)

sngle_creds=500  # Intial value of credits
sngle_bets=0     # and bets

def sngle_credits_add():
  global sngle_creds
  sngle_cred_add = sngle_bets
  sngle_creds += sngle_cred_add
  sngle_creds_counter.set("Credits: ${:.2f}".format(sngle_creds))

def sngle_credits_sub():
  global sngle_creds
  # sngle_scred_sub = sngle_bets
  sngle_creds -= sngle_bets
  sngle_creds_counter.set("Credits: ${:.2f}".format(sngle_creds))
  


def sngle_bets_add():    # For adding bets
  global sngle_bets      # get the intitial value
  sngle_bet_add = sngle_bet_add_sub_var.get() # assign the add subtract intvar to a variable 
  sngle_bets += sngle_bet_add # Add five (sngle_bet_add) to current bet value
  sngle_bets_counter.set("Bets: ${:.2f}".format(sngle_bets)) # format the vale into the counter
  sngle_bet_add_sub_var.set(5) # Makes sure that this variable is set to 5

def sngle_bets_sub(): # For removing bets
  global sngle_bets
  sngle_bet_sub = sngle_bet_add_sub_var.get()
  sngle_bets -= sngle_bet_sub # Subtract five from the current bet value
  sngle_bets_counter.set("Bets: ${:.2f}".format(sngle_bets))
  sngle_bet_add_sub_var.set(5)

sngle_bets_counter = StringVar()  # Sets variable as a string varible
sngle_bets_counter.set("Bets: $0") # Sets the text of the string
sngle_bets_display = Label(sngle_frame, textvariable=sngle_bets_counter, bg="orange",
                   font="Times 10") # Makes the bets counter display
sngle_bets_display.place(x=580, y=100)


sngle_creds_counter = StringVar()
sngle_creds_counter.set("Credits: $500")
sngle_creds_dsiplay = Label(sngle_frame, textvariable=sngle_creds_counter, bg="orange",
                           font="Times 10") # Makes the credits counter display
sngle_creds_dsiplay.place(x=580, y=70)

sngle_bet_add_sub_var=IntVar()  # Assigns this as an intger variable
sngle_bet_add_sub_var.set(5)    # Sets a numerical value
sngle_bet_add_but=Button(sngle_frame, text="Add bets", bg="gold", bd=1, command=sngle_bets_add)
sngle_bet_add_but.place(x=580, y=150) # Button for adding bets
sngle_bet_sub_but=Button(sngle_frame, text="Remove bets", bg="gold", bd=1, command=sngle_bets_sub)
sngle_bet_sub_but.place(x=580, y=180) # Button for removing bets

def sngle_cnfrm_bet():
  sngle_bet_add_but.config(state=DISABLED)
  sngle_bet_sub_but.config(state=DISABLED)
  print(card_num_1, card_num_2) 
  if (card_num_1 + card_num_2) == 6:
    print("You win!!!!")
    sngle_credits_add()
  if (card_num_1 + card_num_2) > 6:
    print("You lose")
    sngle_credits_sub()
  # else:
  #   pass
  # print("Choose an action at the bottom of the screen")

sngle_confirm_bet=Button(sngle_frame, text="Confirm bets", bg="orange", command=sngle_cnfrm_bet)
sngle_confirm_bet.place(x=580, y=220)


sngle_hit_button=Button(sngle_frame, text="Hit", bg="white", bd=1)  # Hit button
sngle_hit_button.place(x=250, y=335)

sngle_stay_button=Button(sngle_frame, text="Stay", bg="white", bd=1)  # Stay button
sngle_stay_button.place(x=375, y=335)

sngle_double_button=Button(sngle_frame, text="Double", bg="white", bd=1)  # Double button
sngle_double_button.place(x=300, y=375)




root.mainloop()  # Loops the program until stopped/exited