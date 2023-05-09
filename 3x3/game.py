import tkinter as tk
import data as d
import function as f


class Interface(tk.Frame):
    """main interface"""

    def __init__(self, **kwargs):
        tk.Frame.__init__(self, **kwargs, background=d.background_color)

        # design
        self.master.title("3x3")
        self.master.geometry('394x430')
        self.master.configure(bg=d.background_color)

        self.grid(sticky="")

        self.player = 1

        self.init_grid()

        self.reset_button = tk.Button(
            self, text="reset", command=self.init_grid)
        self.reset_button.grid(row=3, column=1)

    def init_grid(self):
        """ init the game """

        # data that will need to be reset if the game is reset
        self.finished = False
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        # put the buttons into an array
        self.grid_cells = []

        for i in range(3):
            grid_row = []
            for j in range(3):
                cell = tk.Frame(self, width=50, height=50,
                                bg=d.background_color)

                cell.grid(row=i, column=j, padx=8, pady=8)

                b = tk.Button(master=cell, justify=tk.CENTER, width=15, height=7,
                              relief="groove", bg=d.background_color)
                b.configure(command=lambda button=b: self.click(button))
                b.grid()

                grid_row.append(b)

            self.grid_cells.append(grid_row)

    def click(self, button):
        """change button on click"""

        if self.player == 1:
            button.configure(text=d.player1_sign,
                             bg=d.player1_bg, font=d.font, command=0)

        elif self.player == 2:
            button.configure(text=d.player2_sign,
                             bg=d.player2_bg, font=d.font, command=0)

        self.is_finished(button)

    def is_finished(self, button):
        """know if the game is over or not"""

        # update board
        for i in range(3):
            for j in range(3):
                if button == self.grid_cells[i][j]:
                    if self.player == 1:
                        self.board[i][j] = d.player1_sign
                    elif self.player == 2:
                        self.board[i][j] = d.player2_sign

        # checks if a player has won
        self.finished = f.is_3_aligned(self.board)

        # what is displayed if a player wins
        if self.finished == True:
            self.grid_cells[1][1].configure(
                text=f"Player {self.player} win!", fg="#ffffff")

            for i in range(3):
                for j in range(3):
                    self.grid_cells[i][j].configure(
                        bg=d.background_color, command=0)

        # change player
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1


if __name__ == '__main__':

    # we create our interface
    interface = Interface()
    interface.mainloop()
