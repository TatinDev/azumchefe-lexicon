import tkinter as tk
from tkinter import ttk

from constants import APPLICATION_LABEL, MENU_BAR_LABEL

class AboutDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title(MENU_BAR_LABEL.HELP_ABOUT)
        self.transient(parent)
        self.grab_set()
        self.geometry("360x200")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=16)
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text=APPLICATION_LABEL.TITLE,
            font=("TkHeadingFont", 16, "bold")
        ).pack(pady=(0, 4))

        ttk.Label(
            frame,
            text="Versión 1.0",
            font=("TkDefaultFont", 10)
        ).pack()

        ttk.Label(
            frame,
            text="Editor de léxicos de mapudungun.",
            wraplength=300,
            justify="center",
            font=("TkDefaultFont", 10)
        ).pack(pady=(8, 0))

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=12)

        ttk.Button(
            frame,
            text="Cerrar",
            command=self.destroy
        ).pack()
