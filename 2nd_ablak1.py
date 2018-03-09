#!/usr/bin/env python3
"""
A második

Az első program másolata kibővítve egy Frame objektummal.

Létrehozok a neten talált tutorialok alapján, immár csak az emlékeimre
és a pythonos doksira támaszkodva egy Frame osztályból származtatott
osztályt. Ebből készítek egy új objektumot, amit a "root" objektumhoz adok.
"""


import tkinter as tk

class MyApplication(tk.Frame):

    def __init__(self, root_window):
        super().__init__(root_window)
        self.config(relief=tk.GROOVE, background="#AAAAFF", height=500, width=700)
        self.grid(padx=5, pady=5, sticky="SE" )

def app_start():
    root = tk.Tk()
    #root.geometry("800x600")
    app_object = MyApplication(root)
    root.mainloop()


if __name__ == "__main__":
    app_start()
