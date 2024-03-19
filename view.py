import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import ttk

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
    def GetFrame(self):
        return self
    
    def setController(self, controller):
        self.controller = controller

    