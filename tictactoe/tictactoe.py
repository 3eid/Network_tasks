from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.title("Welcome to The Gaming World: TIC-TAC-TOE")
root.geometry("400x300")

# Add labels for game title and player indicators
title_label = Label(root, text="Tic-Tac-Toe Game", font=('Helvetica', '15'))
title_label.grid(row=0, column=0)
player1_label = Label(root, text="Player 1: X", font=('Helvetica', '10'))
player1_label.grid(row=1, column=0)
player2_label = Label(root, text="Player 2: O", font=('Helvetica', '10'))
player2_label.grid(row=2, column=0)

current_turn = 1  # Track whose turn it is
move_count = 0  # Track number of moves made

def reset_game():
    """Reset the game board and turn."""
    global current_turn, move_count
    current_turn = 1
    move_count = 0
    for button in buttons:
        button["text"] = " "
    print("[*] Game has been reset")

def button_click(button):
    """Handle button click for game play."""
    global current_turn, move_count
    if button["text"] == " ":
        if current_turn == 1:
            button["text"] = "X"
            current_turn = 2
        else:
            button["text"] = "O"
            current_turn = 1
        move_count += 1
        check_winner()

def check_winner():
    """Check if there's a winner or a tie."""
    global move_count
    winning_combinations = [
        (btn1, btn2, btn3),
        (btn4, btn5, btn6),
        (btn7, btn8, btn9),
        (btn1, btn4, btn7),
        (btn2, btn5, btn8),
        (btn3, btn6, btn9),
        (btn1, btn5, btn9),
        (btn3, btn5, btn7),
    ]

    for combination in winning_combinations:
        if combination[0]["text"] == combination[1]["text"] == combination[2]["text"] != " ":
            announce_winner(combination[0]["text"])
            return

    if move_count == 9:
        messagebox.showinfo("Tie", "Match Tied! Try again :)")
        reset_game()

def announce_winner(player):
    """Announce the winner and end the game."""
    message = f"Game complete. {player} wins!"
    messagebox.showinfo("Congratulations", message)
    reset_game()

# Create buttons for the game grid
btn1 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn1))
btn1.grid(column=1, row=1)
btn2 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn2))
btn2.grid(column=2, row=1)
btn3 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn3))
btn3.grid(column=3, row=1)
btn4 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn4))
btn4.grid(column=1, row=2)
btn5 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn5))
btn5.grid(column=2, row=2)
btn6 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn6))
btn6.grid(column=3, row=2)
btn7 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn7))
btn7.grid(column=1, row=3)
btn8 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn8))
btn8.grid(column=2, row=3)
btn9 = Button(root, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: button_click(btn9))
btn9.grid(column=3, row=3)

buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

# Create a reset button
reset_button = Button(root, text="RESET", bg="white", fg="black", width=9, height=1, font=('Helvetica', '20'), command=reset_game)
reset_button.grid(column=1, row=5, columnspan=3, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
