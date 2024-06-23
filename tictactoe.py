import tkinter #tk interface

def checkWinner():
    global turns, winner

    #horizontal
    for column in range(3):
            if (gameboard[0][column]["text"] == gameboard[1][column]["text"] == gameboard[2][column]["text"]
                and gameboard[0][column]["text"] != ""): 
                label.config(text=gameboard[0][column]["text"]+" is the winner!", foreground= "yellow")
                winner = 1
                return


    #vertical
    for row in range(3):
        if (gameboard[row][0]["text"] == gameboard[row][1]["text"] == gameboard[row][2]["text"]
            and gameboard[row][0]["text"] != ""): 
            label.config(text=gameboard[row][0]["text"]+" is the winner!", foreground= "yellow")
            winner = 1
            return

    #diaganol \
    if(gameboard[0][0]["text"] == gameboard[1][1]["text"] == gameboard[2][2]["text"]
       and gameboard[0][0]["text"] != ""):
        label.config(text=gameboard[row][0]["text"]+" is the winner!", foreground= "yellow")
        
        for i in range(3):
            gameboard[i][i]. config(foreground="yellow", background="black")
        
        winner = 1
        return

    #diaganol /
    if(gameboard[0][2]["text"] == gameboard[1][1]["text"] == gameboard[2][0]["text"]
       and gameboard[1][1]["text"] != ""):
        gameboard[0][2]. config(foreground="yellow", background="black")
        gameboard[1][1]. config(foreground="yellow", background="black")
        gameboard[2][0]. config(foreground="yellow", background="black")
        label.config(text=gameboard[row][0]["text"]+" is the winner!", foreground= "yellow")
        winner = 1
        return
    

    if turns == 9:
        label.config(text="tie", foreground= "yellow")
def set_tile(row, column):
    global winner
    if gameboard[row][column]["text"] != "":#stopping from overriding existing marks
        return
    
    if winner == 1:
        return

    global currentPlayer
    global turns
    gameboard[row][column]["text"] = currentPlayer
    if currentPlayer == playerO:
        currentPlayer = playerX
    else: currentPlayer = playerO

    label["text"] = currentPlayer
    turns = turns + 1
    checkWinner()

def newGame():
    global winner, turns
    winner = 0
    turns = 0
    global currentPlayer
    currentPlayer = playerX
    label["text"] = currentPlayer
    for row in range(3):
        for column in range (3):
            gameboard[row][column].config(text="", background = gray, foreground = gray)


playerX = "X"
playerO = "O"
currentPlayer = playerX
winner = 0

gameboard = [0,0,0],[0,0,0],[0,0,0]
maxTurns = 9
turns = 0


blue = "#4584b6" #Change these later
yellow = "#ffde57"
gray = "#343434"
LGray = "#646464"

window = tkinter.Tk() #makes a window
window.title("TTT")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = currentPlayer, font = ("Courier", 20), background = gray, foreground = "white")

label.grid(row = 0, column = 1) #can also do ", columnspan = 3, sticky = "we")" to format nicer

for row in range(3):
    for column in range (3):
        gameboard[row][column] = tkinter.Button(frame, text = "", font = ("Courier", 50, "bold"), 
                                            background = gray, foreground = gray, width = 4, height = 3,
                                            activebackground=gray, highlightbackground=gray,
                                            command = lambda row = row, column = column: set_tile(row, column))
        gameboard[row][column].grid(row = row+1, column = column) #shifting row by 1 to account for the title

button = tkinter.Button(frame, text = "idk", font = ("Courier", 20), background = gray, foreground = "black", 
                        command = newGame)
button.grid(row = 4, column = 1)


frame.pack() #pack organizes the widgets in the window

#for centering the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int(screen_width/2 - window_width/2)
window_y = int(screen_height/2 - window_height/2)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
{
    #
}


