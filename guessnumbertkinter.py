from tkinter import *
from random import randrange
import tkinter.messagebox
import time
import os
from tkinter import messagebox as mb



rt = Tk()
rt.title("NUMBER GUESSING GAME")
rt.geometry("1600x800+0+0")
rt.configure(bg="light green")
###################################################################################################################
Tops=Frame(rt,width = 1600,height = 50,bg="light green",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(rt,width = 550,height = 700,bg="light green",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(rt,width = 300,height = 700,bg="light green",relief=SUNKEN)
f2.pack(side=RIGHT)
########################################################################################################################
lblInfo=Label(Tops,font=("arial",30,"bold"),text="WELCOME TO NUMBER GUESSING GAME",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

lblDateTime=Label(Tops,font=("arial",20,"bold"),text=localtime,bg="dark green",fg="light green",bd=10,anchor="w")
lblDateTime.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="PRESS START BUTTON TO START THE GAME ",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()
#########################################################################################################################
def start():
        global window
        window=Toplevel(rt)
        window.resizable(0, 0)

        window.title("NUMBER GUESSING GAME")
        window.configure(bg="light green")
        global lblInst
        global lblLine0
        global lblNoGuess
        global lblMaxGuess
        global lblLine1
        global lblLogs
        global lblLine2
        global buttons
        global btnStartGameList
        global btnStartGame
        global guess
        global totalNumberOfGuesses
        global secretNumber
        global lblLogs
        global guess_row
        global status
        
        lblInst = Label(window, text = "Guess a number from 0 to 9",bg="light green",fg="dark green")
        lblLine0 = Label(window, text = "*********************************************************************",bg="light green",fg="dark green")
        lblNoGuess = Label(window, text = "No of Guesses: 0",bg="light green",fg="dark green")
        lblMaxGuess = Label(window, text = "Max Guess: 3",bg="light green",fg="dark green")
        lblLine1 = Label(window, text = "*********************************************************************",bg="light green",fg="dark green")
        lblLogs = Label(window, text="Game Logs",bg="light green",fg="dark green")
        lblLine2 = Label(window, text = "*********************************************************************",bg="light green",fg="dark green")

        # create the buttons
        buttons = []
        for index in range(0, 10):
            button = Button(window, text=index, command=lambda index=index : process(index), state=DISABLED,fg="dark green",bg="light green")
            buttons.append(button)


        btnStartGameList = []
        for index in range(0, 1):
            btnStartGame = Button(window, text="Start Game", command=lambda : startgame(index),fg="dark green",bg="light green")
            btnStartGameList.append(btnStartGame)

        # append elements to grid
        lblInst.grid(row=0, column=0, columnspan=5)
        lblLine0.grid(row=1, column=0, columnspan=5)
        lblNoGuess.grid(row=2, column=0, columnspan=3)
        lblMaxGuess.grid(row=2, column=3, columnspan=2)
        lblLine1.grid(row=3, column=0, columnspan=5)
        lblLogs.grid(row=4, column=0, columnspan=5)  # row 4 - 8 is reserved for showing logs

        lblLine2.grid(row=9, column=0, columnspan=5)


        for row in range(0, 2):
            for col in range(0, 5):
                i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
                buttons[i].grid(row=row+10, column=col)

        btnStartGameList[0].grid(row=13, column=0, columnspan=5)

        # Main game logic

        guess = 0
        totalNumberOfGuesses = 0
        secretNumber = randrange(10)
        #print(secretNumber)
        lblLogs = []
        guess_row = 4

        # reset all variables
        def init():
            global buttons, guess, totalNumberOfGuesses, secretNumber, lblNoGuess, lblLogs, guess_row
            guess = 0
            totalNumberOfGuesses = 0
            secretNumber = randrange(10)
            #print(secretNumber)
            lblNoGuess["text"] = "Number of Guesses: 0"
            guess_row = 4

            # remove all logs on init
            for lblLog in lblLogs:
                lblLog.grid_forget()
            lblLogs = []


        def process(i):
            global totalNumberOfGuesses, buttons, guess_row
            guess = i

            totalNumberOfGuesses += 1
            lblNoGuess["text"] = "Number of Guesses: " + str(totalNumberOfGuesses)

            # check if guess match secret number
            if guess == secretNumber:
                lbl = Label(window, text="Your guess was right. You won! :) ", fg="dark green",bg="light green")
                lbl.grid(row=guess_row, column=0, columnspan=5)
                lblLogs.append(lbl)
                guess_row += 1

                for b in buttons:
                    b["state"] = DISABLED
            else:
                # give player some hints
                if guess > secretNumber:
                    lbl = Label(window, text="Secret number is less than your current guess :)", fg="dark green",bg="light green")
                    lbl.grid(row=guess_row, column=0, columnspan=5)
                    lblLogs.append(lbl)
                    guess_row += 1
                else:
                    lbl = Label(window, text="Secret number is greater than your current guess :)", fg="dark green",bg="light green")
                    lbl.grid(row=guess_row, column=0, columnspan=5)
                    lblLogs.append(lbl)
                    guess_row += 1

            # game is over when max no of guesses is reached
            if totalNumberOfGuesses == 3:
                if guess != secretNumber:
                    lbl = Label(window, text="Max guesses reached. You lost! :)", fg="red")
                    lbl.grid(row=guess_row, column=0, columnspan=5)
                    
                    lblLogs.append(lbl)
                    guess_row += 1
                    #print(secretNumber)
                    tkinter.messagebox.showinfo('Result',secretNumber)



                for b in buttons:
                    b["state"] = DISABLED

            buttons[i]["state"] = DISABLED


        status = "none"


        def startgame(i):
            global status
            for b in buttons:
                b["state"] = NORMAL

            if status == "none":
                status = "started"
                btnStartGameList[i]["text"] = "Restart Game"
            else:
                status = "restarted"
                init()
            #print("Game started")




###################################################################################################################
lblInfo=Label(Tops,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

btn15=Button(rt,padx=16,pady=16,bd=8,fg="dark green",font=("arial",18,"bold"),text="START",bg="light green",
                    command=start,anchor="w",width=10,height=0,compound="c")
btn15.place(x=220,y=420)
def call(): 
	res = mb.askquestion('Exit Application', 'Do you really want to exit') 
	
	if res == 'yes' : 
		rt.destroy() 
		
	else : 
		mb.showinfo('Return', 'Returning to main application') 



btn16=Button(rt,padx=16,pady=16,bd=8,fg="dark green",font=("arial",18,"bold"),text="Quit",bg="light green",
                    command=call,anchor="w",width=10,height=0,compound="c")
btn16.place(x=620,y=420)


rt.mainloop()
