import tkinter as tk
import data as d
import function as f


class Interface(tk.Frame):
    """main interface"""

    def __init__(self, **kwargs):
        tk.Frame.__init__(self, **kwargs, background="#000000")

        # design
        self.master.title("9x9")
        self.master.configure(bg=d.background_color)

        self.grid(sticky="")

        self.player = 1

        self.init_grid()

        self.reset_button = tk.Button(
            self, text="reset", bg=d.background_color, fg="#ffffff", command=self.init_grid)
        self.reset_button.grid(ipadx=30, ipady=10, row=3, column=1, pady=5)

    def init_grid(self):
        """initialization of 2 empty 9x9 grid (one with buttons and another with 0)
        we save the variable of each small box in one_board (all the variables of one big cell)
        and then we save one_board in  self.grid_cells

        we'll have something like this :
        [[button0, button1, button2,         [button9, button10, button11,        [button18, button19, button20,
          button3, button4, button5,          button12, button13, button14,        button21, button22, button23,
          button6, button7, button8],         button15, button16, button17],       button24, button25, button26],

         [button27, button28, button29,      [button36, button37, button38,       [button45, button46, button47,
          button30, button31, button32,       button39, button40, button41,        button48, button49, button50,
          button33, button34, button35],      button42, button43, button44],       button51, button52, button53],

         [button54, button55, button56,      [button63, button64, button65,       [button72, button73, button74,
          button57, button58, button59,       button66, button67, button68,        button75, button76, button77,
          button60, button61, button62],      button69, button70, button71],       button78, button79, button80],

                                AND (same but with 0)

        [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        """

        # data that will need to be reset if the game is reset
        self.finished = False

        # put the buttons into an array
        self.grid_cells = []  # Grid with button
        self.board = []  # Grid fill with 0
        for i in range(3):
            for j in range(3):

                # creation of a big cell
                big_cell = tk.Frame(
                    self, width=500, height=500, borderwidth=1, bg=d.background_color)
                big_cell.grid(row=i, column=j, padx=4, pady=4)

                one_cell = []
                one_board = []
                for k in range(3):
                    for l in range(3):

                        # add little cells inside the big cell
                        little_cell = tk.Frame(
                            big_cell, width=30, height=30, bg=d.background_color)
                        little_cell.grid(
                            row=k, column=l, padx=4, pady=4)

                        button = tk.Button(master=little_cell, justify=tk.CENTER, width=5, height=2,
                                           relief="groove", bg="#0d0c0c", fg="#000000")
                        button.configure(
                            command=lambda button=button: self.click(button))
                        button.grid()

                        # add button inside one_cell
                        one_cell.append(button)
                        one_board.append(0)
                # add nbr_var_list inside one_cell
                self.grid_cells.append(one_cell)
                self.board.append(one_board)

        # Text who display when a player has won
        self.text_finished = tk.Label(self, bg=d.background_color, fg="#ffffff", font=(
            "Arial, sans-serif", 19, "bold"))

        self.text_finished.grid_forget()

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
        for i in range(9):
            for j in range(9):
                if button == self.grid_cells[i][j]:
                    if self.player == 1:
                        self.board[i][j] = d.player1_sign
                    elif self.player == 2:
                        self.board[i][j] = d.player2_sign

                    next_position = j  # get the position to know where to play next

                # put the grid back normally
                if len(self.board[i]) != 1:
                    if self.board[i][j] == 0:
                        self.grid_cells[i][j].configure(
                            state="normal", relief="groove", bg="#0d0c0c")

        # return a board and True or False
        self.board, self.finished = f.is_a_board_finished(
            self.board, self.player)

        # disable all buttons that the next player shouldn't be playing
        if len(self.board[next_position]) != 1:
            for i in range(9):
                # check if the big grid isn't marked by a player
                if len(self.board[i]) != 1:
                    for j in range(9):

                        # check that the buttons are not the next to be chosen and that they are not marked
                        if self.grid_cells[i] != self.grid_cells[next_position] and self.board[i][j] == 0:
                            self.grid_cells[i][j].configure(
                                state="disabled", relief="sunken", bg=d.background_color)

        counter = 0
        # change the interface board
        for item in self.board:

            if item == d.player1_sign:
                i = 0
                for btn in self.grid_cells[counter]:
                    if i % 2 == 0:
                        btn.configure(text="", bg=d.player1_bg,
                                      relief="flat", state="disabled", command=0)
                    else:
                        btn.configure(text="", bg=d.background_color,
                                      relief="flat", state="disabled", command=0)
                    i += 1

            elif item == d.player2_sign:
                i = 0
                for btn in self.grid_cells[counter]:
                    if i % 2 != 0:
                        btn.configure(text="", bg=d.player2_bg,
                                      relief="flat", state="disabled", command=0)
                    else:
                        btn.configure(text="", bg=d.background_color,
                                      relief="flat", state="disabled", command=0)
                    i += 1
      

            #ICI JE DOIS GRISER LES CASES EN CAS DE MATCH NUL
            elif item == "G":
                for btn in self.grid_cells[counter]:
                     btn.configure(bg="#d9d9d9", relief="flat", state="disabled", command=0)

            
            counter += 1

        # If the game is entirely over
        if self.finished == True:

            # make the text visible
            self.text_finished.configure(
                text=f"Player {self.player} win!")

            self.text_finished.grid(row=1, column=1)

            # Hide buttons
            for i in range(len(self.board)):
                for btn in self.grid_cells[i]:
                    btn.grid_forget()

        # change player
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1


if __name__ == '__main__':

    # we create our interface
    interface = Interface()
    interface.mainloop()
