#!/usr/bin/env python3
"""
A második

Az első program másolata kibővítve egy Frame objektummal.

Létrehozok a neten talált tutorialok alapján, immár csak az emlékeimre
és a pythonos doksira támaszkodva egy Frame osztályból származtatott
osztályt. Ebből készítek egy új objektumot, amit a "root" objektumhoz adok.

Ahhoz, hogy a Frame mérete a root-éhoz igazodjon, a pack használata tűnik szükségesnek,
ezen belül pedig az expand=Y és fill=BOTH paramétereké.
De mint kantal-tól (https://hup.hu/node/158324#comment-2207526) megtudtam, grid-del is működik
a dolog. A lényeg, hogy a grid megfelelő cellájánál (column és row egyaránt) a weight nagyobb
legyen, mint nulla.
A relief működéséhez a defaultnál vastagabb border szükséges (bd=3 pl.)
"""


import tkinter as tk


class MyApplication(tk.Frame):

    def __init__(self, root_window):
        super().__init__(root_window)


def app_start():
    root = tk.Tk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    app_object = MyApplication(root)
    app_object.config(relief=tk.GROOVE, bd=3, background="#AAAAFF", height=500, width=700)
    app_object.grid(row=0,column=0,padx=5,pady=5,sticky="NWSE")
    root.mainloop()


if __name__ == "__main__":
    app_start()
