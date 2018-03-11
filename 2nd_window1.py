#!/usr/bin/env python3
"""
A második

Az első program másolata kibővítve egy Frame objektummal.

Létrehozok a neten talált tutorialok alapján, immár csak az emlékeimre
és a pythonos doksira támaszkodva egy Frame osztályból származtatott
osztályt. Ebből készítek egy új objektumot, amit a "root" objektumhoz adok.

Ahhoz, hogy a Frame mérete a root-éhoz igazodjon, a pack használata tűnik szükségesnek,
ezen belül pedig az expand=Y és fill=BOTH paramétereké.
A relief működéséhez a defaultnál vastagabb border szükséges (bd=3 pl.)
"""


import tkinter as tk


class MyApplication(tk.Frame):

    def __init__(self, root_window):
        super().__init__(root_window)


def app_start():
    root = tk.Tk()
    app_object = MyApplication(root)
    app_object.config(relief=tk.GROOVE, bd=3, background="#AAAAFF", height=500, width=700)
    app_object.pack(padx=5, pady=5, expand=tk.Y, fill=tk.BOTH)
    root.mainloop()


if __name__ == "__main__":
    app_start()
