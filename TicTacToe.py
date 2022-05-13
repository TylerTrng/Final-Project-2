from tkinter import *
from tkinter import messagebox


root = Tk()
root.resizable(False, False)
root.title('TIC TAC TOE')
clicked = True
count = 0
def end_game():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
def winner_check():
        global X_point, O_point
        if count == 9:
                messagebox.showinfo('Message!!!', 'The Game Is Tie!!!')
                reset_game()
        #Cross O Win  
        if (b1["text"]=="O") and (b5["text"]=="O") and (b9["text"]=="O"):
                b1.config(bg="red")
                b5.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point)) 
                end_game()

        if b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
                b3.config(bg="red")
                b5.config(bg="red")
                b7.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()
        #Verticle O Win
        if (b1["text"]=="O") and (b4["text"]=="O") and (b7["text"]=="O"):
                b1.config(bg="red")
                b4.config(bg="red")
                b7.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()

        if b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
                b2.config(bg="red")
                b5.config(bg="red")
                b8.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()

        if b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
                b3.config(bg="red")
                b6.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()
        #Horizontal O Win
        if (b1["text"]=="O") and (b2["text"]=="O") and (b3["text"]=="O"):
                b1.config(bg="red")
                b2.config(bg="red")
                b3.config(bg="red")
                winner = True
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()

        if b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
                b4.config(bg="red")
                b5.config(bg="red")
                b6.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()

        if b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
                b7.config(bg="red")
                b8.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo('Message!!!', 'O Win!')
                O_point += 1
                o_score.config(text="O: " + str(O_point))
                end_game()

        #Cross X Win
        if (b1["text"]=="X") and (b5["text"]=="X") and (b9["text"]=="X"):
                b1.config(bg="red")
                b5.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()

        if b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
                b3.config(bg="red")
                b5.config(bg="red")
                b7.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()
        #Verticle X Win
        if (b1["text"]=="X") and (b4["text"]=="X") and (b7["text"]=="X"):
                b1.config(bg="red")
                b4.config(bg="red")
                b7.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()

        if b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
                b2.config(bg="red")
                b5.config(bg="red")
                b8.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()

        if b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
                b3.config(bg="red")
                b6.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()
        #Horizontal X Win
        if (b1["text"]=="X") and (b2["text"]=="X") and (b3["text"]=="X"):
                b1.config(bg="red")
                b2.config(bg="red")
                b3.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()

        if b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
                b4.config(bg="red")
                b5.config(bg="red")
                b6.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()

        if b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
                b7.config(bg="red")
                b8.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo('Message!!!', 'X Win!')
                X_point += 1
                x_score.config(text="X: " + str(X_point))
                end_game()

def b_click(b):
    global clicked, count
    if b["text"] == "" and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    elif b["text"] == "" and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
    else:
        messagebox.showerror('Tic Tac Toe', 'This box is already clicked')
    if count >= 3:
        winner_check()

#Button Builds 
def reset_game():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count
        clicked = True
        count = 0
        b1 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b1))
        b1.grid(row=0, column=0)
        b2 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b2))
        b2.grid(row=0, column=1)
        b3 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b3))
        b3.grid(row=0, column=2)

        b4 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b4))
        b4.grid(row=1, column=0)
        b5 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b5))
        b5.grid(row=1, column=1)
        b6 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b6))
        b6.grid(row=1, column=2)

        b7 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b7))
        b7.grid(row=2, column=0)
        b8 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b8))
        b8.grid(row=2, column=1)
        b9 = Button(root, text="", font=("Times New Roman", 20), height=3, width=6, bg="White", command=lambda: b_click(b9))
        b9.grid(row=2, column=2)
        
reset_button = Button(root, text="Reset", font=("Times New Roman", 20), height=1, width=6, bg="White", command=reset_game)
reset_button.grid(row=3, column=1)
X_point = 0
O_point = 0
x_score = Label(root, text="X: " + str(X_point))
x_score.grid(row=3, column=0)
o_score = Label(root, text="O: " + str(O_point))
o_score.grid(row=3, column=2)

reset_game()
root.mainloop()
