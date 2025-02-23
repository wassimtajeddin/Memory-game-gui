import tkinter as tk

root = tk.Tk()
root.title("Memory Game")
root.geometry("400x300")

title = tk.Label(root, text="Memory Game", font=("Arial", 16))
title.pack(pady=20)

root.mainloop()
