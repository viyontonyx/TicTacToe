import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):  # Corrected __init__ method name
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [' ']*9

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(root, text=' ', width=10, height=4, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, i, j):
        if self.board[i*3 + j] == ' ':
            self.board[i*3 + j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.current_player = 'X'
        self.board = [' ']*9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
