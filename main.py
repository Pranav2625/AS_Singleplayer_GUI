from tkinter import *
from functools import partial
import random # For randint function

def sngle_generate():
  global sngle_card_play_1
  global sngle_card_play_2
  global sngle_hit_card
  global sngle_card_play_ttl
  global sngle_card_deal_1
  global sngle_card_deal_2
  global sngle_card_deal_ttl
  sngle_card_play_1 = random.randint(1, 5) # Make two random cards that
  sngle_card_play_2 = random.randint(1, 5) # will be used for the player
  sngle_hit_card = random.randint(1, 5) # Used for hit
  sngle_card_play_ttl = (sngle_card_play_1 + sngle_card_play_2) # Total for player cards
  sngle_card_deal_1 = random.randint(1, 5) # Make two random cards for 
  sngle_card_deal_2 = random.randint(1, 5) # the dealer
  sngle_card_deal_ttl = (sngle_card_deal_1 + sngle_card_deal_2) # Total for dealer cards
  sngle_cnfrm_bet()

root = Tk()
root.title("Single Player Mode")  # Window title

sngle_frame = Frame(root, width=700, height=500, bg="green")  # Window Frame
sngle_frame.grid()

dealer_side = Label(sngle_frame, text="Dealer", font="Times 14 bold",  # Dealer's Side
                    bg="#733f19", fg="white", padx=330, pady=12)  # of the table
dealer_side.place(x=-10, y=0)

sngle_creds = 500  # Intial value of credits
sngle_bets = 0  # and bets


def sngle_credits_add():
    global sngle_creds   # Get the credits count
    sngle_cred_add = sngle_bets # Variable that stores players bets
    sngle_creds += sngle_cred_add # Add the bets to the credits
    sngle_creds_counter.set("Credits: ${:.2f}".format(sngle_creds)) # Format 
                                                          # it into the counter

def sngle_credits_sub():
    global sngle_creds  # Get credits count
    # sngle_scred_sub = sngle_bets
    sngle_creds -= sngle_bets  # Subtract the bet amount from the credits
    sngle_creds_counter.set("Credits: ${:.2f}".format(sngle_creds)) # Format it
                                                                  # it into counter


def sngle_bets_add():  # For adding bets
    global sngle_bets  # get the intitial value
    sngle_bet_add = sngle_bet_add_sub_var.get()  # assign the add subtract intvar to a variable
    sngle_bets += sngle_bet_add  # Add five (sngle_bet_add) to current bet value
    sngle_bets_counter.set("Bets: ${:.2f}".format(sngle_bets))  # format the value into the counter
    sngle_bet_add_sub_var.set(5)  # Makes sure that this variable is set to 5


def sngle_bets_sub():  # For removing bets
    global sngle_bets
    sngle_bet_sub = sngle_bet_add_sub_var.get()
    sngle_bets -= sngle_bet_sub  # Subtract five from the current bet value
    sngle_bets_counter.set("Bets: ${:.2f}".format(sngle_bets))  # format value into counter
    sngle_bet_add_sub_var.set(5)




sngle_bets_counter = StringVar()  # Sets variable as a string varible
sngle_bets_counter.set("Bets: $0")  # Sets the text of the string
sngle_bets_display = Label(sngle_frame, textvariable=sngle_bets_counter, bg="orange",
                           font="Times 10")  # Makes the bets counter display
sngle_bets_display.place(x=580, y=100)

sngle_creds_counter = StringVar()
sngle_creds_counter.set("Credits: $500")
sngle_creds_dsiplay = Label(sngle_frame, textvariable=sngle_creds_counter, bg="orange",
                            font="Times 10")  # Makes the credits counter display
sngle_creds_dsiplay.place(x=580, y=70)

sngle_bet_add_sub_var = IntVar()  # Assigns this as an intger variable
sngle_bet_add_sub_var.set(5)  # Sets a numerical value
sngle_bet_add_but = Button(sngle_frame, text="Add bets", bg="gold", bd=1, command=sngle_bets_add)
sngle_bet_add_but.place(x=580, y=150)  # Button for adding bets
sngle_bet_sub_but = Button(sngle_frame, text="Remove bets", bg="gold", bd=1, command=sngle_bets_sub)
sngle_bet_sub_but.place(x=580, y=180)  # Button for removing bets


def sngle_cnfrm_bet():
    sngle_bet_add_but.config(state=DISABLED) # Disbale add bets
    sngle_bet_sub_but.config(state=DISABLED) # remove bets
    sngle_confirm_bet.config(state=DISABLED) # and confirm bet buttons
    print("Your cards:",sngle_card_play_1, sngle_card_play_2) # Print the players cards
    if (sngle_card_play_ttl) == 9: # If the card total is equal to nine
        print("You win!!!!") # print this statement
        sngle_bet_add_but.config(state=NORMAL) # revert the buttons back to normal
        sngle_bet_sub_but.config(state=NORMAL)
        sngle_confirm_bet.config(state=NORMAL)
        sngle_credits_add()  # Add bets to credits
    if (sngle_card_play_ttl) > 9: # If the card total is over nine
        print("You lose") # print this
        sngle_bet_add_but.config(state=NORMAL) # revert the buttons back to normal
        sngle_bet_sub_but.config(state=NORMAL)
        sngle_confirm_bet.config(state=NORMAL)
        sngle_credits_sub() # Take away bets amount from credits
    if (sngle_card_play_ttl) < 9: # If the total is less than nine
        print("Choose an action at the bottom of the screen")
        pass # Continue the game using actions


def sngle_play(): 
    print("Dealer's Cards:",sngle_card_deal_1, sngle_card_deal_2) # Print the dealers cards
    if sngle_card_play_ttl > sngle_card_deal_ttl: # If the players total exceeds deealers ttl
        if sngle_card_play_ttl < 9:  # and is less than nine
            print("You win") # they win
            sngle_credits_add()  # and add winnings to credits
        if sngle_card_play_ttl > 9: # or is more than nine
            print("You lose")  # they lose
            sngle_credits_sub() # and takes away credits
    if sngle_card_play_ttl < sngle_card_deal_ttl: # If the dealers total exceeds the players ttl
        print("You lose")  # they lose
        sngle_credits_sub() # and takes away credits
    if sngle_card_play_ttl == sngle_card_deal_ttl:
        print("Draw")
    sngle_bet_add_but.config(state=NORMAL) # revert the buttons back to normal
    sngle_bet_sub_but.config(state=NORMAL)
    sngle_confirm_bet.config(state=NORMAL)


def sngle_hit():
  global sngle_card_play_ttl # Get the player card total
  sngle_card_play_ttl += sngle_hit_card # Add another card to it
  print("Your cards:",sngle_card_deal_1, sngle_card_deal_2, sngle_hit_card) # print the cards
  if sngle_card_play_ttl == 9:  # if the players cards total nine
      print("You win") # They win
      sngle_credits_add() # and get their winnings added to their credits
  if sngle_card_play_ttl > 9:
      print("You lose")
      sngle_credits_sub()
  else: 
    sngle_play() 

def sngle_dbledwn():
  global sngle_bets # Get player bets
  sngle_bets *= 2 # Multiply it by two
  sngle_bets_counter.set("Bets: ${:.2f}".format(sngle_bets)) # and format it
  sngle_play()

sngle_confirm_bet = Button(sngle_frame, text="Confirm bets", bg="orange", command=sngle_generate)
sngle_confirm_bet.place(x=580, y=220) # Confirm bet button

sngle_hit_button = Button(sngle_frame, text="Hit", bg="white", bd=1, command=sngle_hit)  # Hit button
sngle_hit_button.place(x=250, y=335)

sngle_stay_button = Button(sngle_frame, text="Stay", bg="white", bd=1, command=sngle_play)  # Stay button
sngle_stay_button.place(x=375, y=335)

sngle_double_button = Button(sngle_frame, text="Double", bg="white", bd=1, command=sngle_dbledwn)  # Double button
sngle_double_button.place(x=300, y=375)


sngle_exit_but = Button(sngle_frame, text="Exit", bg="orange",bd=1)
sngle_exit_but.place(x=580, y=375)


root.mainloop()  # Loops the program until stopped/exited