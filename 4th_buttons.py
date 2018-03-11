#!/usr/bin/env python3
"""
Button widgetek

Valami új valami szép: Button widgetek használatának demója/tesztje

A feladvány: sötétszürke alapokra helyezett Frame, rajta két Button.
Az egyik aktív, a másik inaktív.
Ha az egyikre kattintok, a gomb inaktívvá válik és a másikat aktiválja.
És viszont.
Sajnos nem találtam a Google-n olyan lehetőséget, hogy a command= által meghatározott
függvény/metódus lekérdezze, hogy mely gomb lenyomása indította el.
Kerülőútként lambda fv.-t lehet használni, amiből meg tudom hívni a szükséges fv.-t
paraméterrel. Ott pedig át tudom adni, hogy mely gomb lett lenyomva (melyiket kell letiltani)
és melyiket kell engedélyezni.
"""

import tkinter as tk


class MyApplication(tk.Frame):
    def __init__(self, root_window, *cnf, **kw):
        super().__init__(root_window, *cnf, **kw)
        self.b1 = None  # Nem szükséges, csak a PyCharm pampog miatta,
        self.b2 = None  # hogy a self.xxx változó nincs definiálva az __init__-ben.
        self.setup_gui()
        self.grid(padx=5, pady=5, sticky="NWSE")

    def setup_gui(self):
        tk.Label(self, text="   <<< Left   ").grid(row=0, column=0)
        self.b1 = tk.Button(self, text="1 - Activate 2",
                            command=lambda: self.click(self.b1, self.b2))
        self.b1.grid(row=0, column=1)
        tk.Label(self, text="  <<< Center >>>  ").grid(row=0, column=2)
        self.b2 = tk.Button(self, text="2 - Activate 1", state=tk.DISABLED,
                            command=lambda: self.click(self.b2, self.b1))
        self.b2.grid(row=0, column=3)
        tk.Label(self, text="   <<< Left   ").grid(row=0, column=4)

    def click(self, button_to_disable, button_to_enable):
        button_to_disable.configure(state=tk.DISABLED)
        button_to_enable.configure(state=tk.NORMAL)


def app_start():
    root_window = tk.Tk()
    root_window.columnconfigure(0, weight=1)
    root_window.rowconfigure(0, weight=1)
    app_frame = MyApplication(root_window, width=800, height=600, bd=3, relief=tk.GROOVE,
                              background="#333333", padx=25, pady=25)
    root_window.mainloop()


if __name__ == "__main__":
    app_start()
