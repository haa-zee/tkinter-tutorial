#!/usr/bin/env python3
"""
Ez lesz a legelső tkinter program

A feladata annyi, hogy kirak egy üres ablakot a képernyőre,
800x600px méretben.

A tkinter-t használó programok alapja:
- importálni a tkinter csomagot
- létrehozni egy Tk objektumot
- a létrehozott objektum mainloop metódusát futtatni.
"""


import tkinter as tk


def app_start():
    root = tk.Tk()
    root.geometry("800x600")
    root.mainloop()


if __name__ == "__main__":
    app_start()
