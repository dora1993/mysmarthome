import tkinter as tk


class TemperatureModule(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)

        self.create_test_label()
    
    def create_test_label(self):
        self.test_label = tk.Label(self, text="Temperature", font=self.font)
        self.test_label.grid(row=0, column=0)