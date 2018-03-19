#!/usr/bin/env python3
"""
Beviteli mezők kezelése

!!!!!!!! Ez már nem működik, itt félbehagytam a tkinter tanulmányozását, a gyengének tűnő dokumentáltság miatt !!!!!

...
"""

import tkinter as tk


class AppWindow(tk.Frame):
    def __init__(self, root_window, *cnf, **kwargs):
        super().__init__(root_window, *cnf, **kwargs)
        self.setup_gui()

    def setup_gui(self):
        tk.Label(self, text="Mező neve:").grid(row=0, column=0, sticky=tk.E)
        self.e1 = tk.Entry(self)
        self.e1.grid(row=0, column=2, padx=5, pady=5)
        is_it_valid = (self.register(self.check_entry), "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")
        self.e1.configure(validate="focus", validatecommand=is_it_valid, invalidcommand=self.invalid)

        self.b1 = tk.Button(self, text="Send")
        self.b1.grid(row=3, column=0, columnspan=4, sticky="NWSE")
        self.b1.configure(command=lambda: self.do_something())

    def do_something(self):
        print("Csinálok valamit")

    def check_entry(self, type, index_of_char, p_value, prior_edit, text_inserted, type_of_validation,
                    validation_triggered, name_of_widget):
        print(p_value," - ",p_value.isalpha())
        return p_value.isalpha()

    def invalid(self):
        print("Invalid...")
        return

def start_app():
    root_window = tk.Tk()
    root_window.columnconfigure(0, weight=1)
    root_window.rowconfigure(0, weight=1)
    app = AppWindow(root_window, width=800, height=600)
    app.configure(bd=3, padx=10, pady=10, bg="#8888AA", relief=tk.GROOVE)
    app.grid()
    app.grid_propagate(0)
    root_window.mainloop()


if __name__ == "__main__":
    start_app()
