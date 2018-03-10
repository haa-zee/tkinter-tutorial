#!/usr/bin/env python3
"""
A harmadik...

A 2nd_ablak1.py alapján készül. Egy 4x4-es grid létrehozása a feladvány,
némi dekorációval, a rács elemei Button ojjektumok.
A grid() sticky paramétere adja meg, hogy melyik oldalon ragadjon a cella oldala,
ha változik a cellát tartalmazó widget mérete. (N=North, S=South, W=West, E=East -
amennyiben két szemben lévő oldalt egyszerre állítok be, akkor abban az irányban
a konténer méretének változásakor a widget mérete is változik, NS esetében a függőleges,
WE esetében a vízszintes, NSWE esetében minden irányban)
"""


import tkinter as tk


class MyApplication(tk.Frame):

    def __init__(self, root_window):
        super().__init__(root_window)
        self.run_flag = False

    def add_cells(self):
        if self.run_flag:
            return
        self.run_flag = True
        for i in range(0, 4):
            for j in range(0, 4):
                self.columnconfigure(i, weight=1)
                self.rowconfigure(j, weight=1)
                widget = tk.Button(self, text="{}x{}".format(i,j))
                widget.grid(column=i, row=j, sticky="WE", padx=4, pady=4)


def app_start():
    root = tk.Tk()
    root.geometry("800x600")
    app_object = MyApplication(root)
    app_object.config(relief=tk.GROOVE, bd=3, background="#AAAAFF")
    app_object.pack(padx=5, pady=5, ipadx=5, ipady=5, expand=tk.Y, fill=tk.BOTH)
    app_object.add_cells()
    root.mainloop()


if __name__ == "__main__":
    app_start()
