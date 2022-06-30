import tkinter as tk
from tkinter import ttk

from lights.gui import  LightsModule
from security.gui import SecurityModule
from temperature.gui import TemperatureModule
from tv.gui import TVModule


class MySmartHome(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algebra | MySmartHome")
        self.geometry("800x600")

        self.apply_custom_style()
        self.create_tab_navigation()
    
    def apply_custom_style(self):
        self.style = ttk.Style()
        self.style.theme_create(
            "MySmartHomeTheme", settings={
                "TNotebook": {
                    "configure": {
                        "tabmargins": [5, 5, 5, 5]
                    }
                },
                "TNotebook.Tab": {
                    "configure": {
                        "padding": [15, 15],
                        "background": "#FF7332"
                    },
                    "map": {
                        "background": [("selected", "#F88B62")],
                        "expand": [("selected", [1, 1, 1, 0])]
                    }
                }
            }
        )
        self.style.theme_use("MySmartHomeTheme")

    def create_tab_navigation(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0)

        self.tv_frame = TVModule(self)
        self.tv_frame.grid(row=0, column=1)
        self.notebook.add(self.tv_frame, text="TV")

        self.lights_frame = LightsModule(self)
        self.lights_frame.grid(row=0, column=1)
        self.notebook.add(self.lights_frame, text="Lights")

        self.security_frame = SecurityModule(self)
        self.security_frame.grid(row=0, column=1)
        self.notebook.add(self.security_frame, text="Security")

        self.temperature_frame = TemperatureModule(self)
        self.temperature_frame.grid(row=0, column=1)
        self.notebook.add(self.temperature_frame, text="Temperature")


root = MySmartHome()

root.mainloop()
