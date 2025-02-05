This project is a **Tic Tac Toe game** implemented using **Python** and the **Tkinter** library for creating graphical user interfaces (GUIs). Here's an overview of how it works:

# Key Features:**
1. **Game Board:**
   - The game board consists of a 3x3 grid created with `tk.Button` widgets.
   - Each button represents a cell where players can place their moves ('X' or 'O') by clicking on the button.

2. **Gameplay:**
   - The game alternates turns between two players: Player 'X' and Player 'O'.
   - When a player clicks a button, their respective symbol ('X' or 'O') is placed in that cell.
   - After each move, the game checks for a winner or a draw.

3. **Winner Detection:**
   - The game checks for a winner after each move. A player wins if they align three of their symbols horizontally, vertically, or diagonally.
   - If there is a winner, a popup message is displayed, announcing the winning player.

4. **Draw Detection:**
   - If the board is filled, and there is no winner, a draw is declared.

5. **Game Reset:**
   - After a win or draw, the game automatically resets the board for a new round.

### **Components of the Code:**
1. **TicTacToe Class:**
   - Manages the core logic of the game: keeping track of the board, switching turns, and checking for winners or draws.
   - Contains methods like:
     - `on_button_click(i, j)`: Handles a player's move when a button is clicked.
     - `check_winner()`: Checks if a player has won the game.
     - `reset_game()`: Resets the game to its initial state after a win or draw.

2. **GUI Setup:**
   - The GUI is built using `tkinter` where a 3x3 grid of buttons is created, each linked to the `on_button_click` method.
   - The window title is set to "Tic Tac Toe" and has the layout arranged using the `grid` method.

3. **Message Boxes:**
   - The `messagebox.showinfo` function is used to display popups when a player wins or when the game ends in a draw.

### **How to Play:**
- Two players alternate placing their moves ('X' and 'O') by clicking on empty cells on the 3x3 grid.
- The game announces the winner once a player successfully aligns three of their symbols in a row, column, or diagonal.
- If all cells are filled without a winner, it declares a draw.

### **Improvements to Consider:**
- Adding a score counter to track wins for both players.
- Implementing an option to restart the game manually without waiting for the game to end.
- Improving the AI for single-player mode, where a user can play against the computer.

Overall, this project serves as a fun, interactive way to practice programming with Python, and it provides a simple but effective GUI using Tkinter for anyone learning to build desktop applications.
