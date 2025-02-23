import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.root.geometry("400x300")

        self.cards = list(range(1, 9)) * 2
        random.shuffle(self.cards)
        self.flipped = []

        self.title = tk.Label(root, text="Memory Game", font=("Arial", 16))
        self.title.grid(row=0, column=0, columnspan=4, pady=20)

        self.buttons = []
        for row in range(1, 5):
            for col in range(4):
                index = (row - 1) * 4 + col
                btn = tk.Button(root, text="", width=6, height=3, command=lambda r=row, c=col: self.flip_card(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(btn)

    def flip_card(self, row, col):
        index = (row - 1) * 4 + col
        if self.buttons[index]["text"] == "" and len(self.flipped) < 2:
            self.buttons[index].config(text=self.cards[index])
            self.flipped.append((row, col))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        (row1, col1), (row2, col2) = self.flipped
        index1 = (row1 - 1) * 4 + col1
        index2 = (row2 - 1) * 4 + col2
        if self.cards[index1] == self.cards[index2]:
            self.buttons[index1].config(state=tk.DISABLED)
            self.buttons[index2].config(state=tk.DISABLED)
        else:
            self.buttons[index1].config(text="")
            self.buttons[index2].config(text="")
        self.flipped = []

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()