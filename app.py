import tkinter as tk

root = tk.Tk()
root.title("Memory Game")
root.geometry("400x300")

title = tk.Label(root, text="Memory Game", font=("Arial", 16))
title.grid(row=0, column=0, columnspan=4, pady=20)

buttons = []
for row in range(1, 5):
    for col in range(4):
        btn = tk.Button(root, text="", width=6, height=3)
        btn.grid(row=row, column=col, padx=5, pady=5)
        buttons.append(btn)

root.mainloop()