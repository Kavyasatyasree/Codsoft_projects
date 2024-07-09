from tkinter import *
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x400")
        self.root.configure(bg="grey")
        self.root.title("Rock Paper Scissors Game")

        self.computer_choices = {
            0: "Rock",
            1: "Paper",
            2: "Scissors"
        }

        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text="Rock Paper Scissors", font="normal 20 bold", fg="blue", bg="grey").pack(pady=20)

        frame = Frame(self.root, bg="grey")
        frame.pack()

        self.player_label = Label(frame, text="Player", font="normal 12", bg="grey")
        self.vs_label = Label(frame, text="vs", font="normal 12 bold", bg="grey")
        self.computer_label = Label(frame, text="Computer", font="normal 12", bg="grey")

        self.player_label.pack(side=LEFT, padx=10)
        self.vs_label.pack(side=LEFT)
        self.computer_label.pack()

        self.result_label = Label(self.root, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
        self.result_label.pack(pady=20)

        frame_buttons = Frame(self.root, bg="grey")
        frame_buttons.pack()

        self.rock_button = Button(frame_buttons, text="Rock", font="normal 10", width=7, command=lambda: self.play_game(0))
        self.paper_button = Button(frame_buttons, text="Paper", font="normal 10", width=7, command=lambda: self.play_game(1))
        self.scissors_button = Button(frame_buttons, text="Scissors", font="normal 10", width=7, command=lambda: self.play_game(2))

        self.rock_button.pack(side=LEFT, padx=10)
        self.paper_button.pack(side=LEFT, padx=10)
        self.scissors_button.pack(padx=10)

        self.reset_button = Button(self.root, text="Reset Game", font="normal 10", fg="red", bg="black", command=self.reset_game)
        self.reset_button.pack(pady=20)

    def play_game(self, player_choice):
        computer_choice = random.randint(0, 2)
        result, computer_choice_text = self.determine_winner(player_choice, computer_choice)
        self.display_results(player_choice, computer_choice, result, computer_choice_text)
        self.disable_buttons()

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Draw", self.computer_choices[computer_choice]
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            return "Player Wins", self.computer_choices[computer_choice]
        else:
            return "Computer Wins", self.computer_choices[computer_choice]

    def display_results(self, player_choice, computer_choice, result, computer_choice_text):
        self.player_label.config(text=f"Player: {self.computer_choices[player_choice]}")
        self.vs_label.config(text="vs")
        self.computer_label.config(text=f"Computer: {computer_choice_text}")
        self.result_label.config(text=result)

    def disable_buttons(self):
        self.rock_button.config(state=DISABLED)
        self.paper_button.config(state=DISABLED)
        self.scissors_button.config(state=DISABLED)

    def reset_game(self):
        self.result_label.config(text="")
        self.player_label.config(text="Player")
        self.vs_label.config(text="")
        self.computer_label.config(text="Computer")
        self.rock_button.config(state=NORMAL)
        self.paper_button.config(state=NORMAL)
        self.scissors_button.config(state=NORMAL)

if __name__ == "__main__":
    root = Tk()
    game = RockPaperScissors(root)
    root.mainloop()
