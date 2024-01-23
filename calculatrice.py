import tkinter as tk

def create_button(master, text, row, col, command):
    tk.Button(master, text=text, command=command, width=5, height=2).grid(row=row, column=col, sticky="nsew")