import tkinter as tk

from typing import Callable, Literal, Optional

from views.common.button_frame import ButtonFrame

from constants import COLOR

class EntryFrame(tk.Frame):
    def __init__(
            self, 
            parent, 
            buttonstyle: Literal['', 'accent'] = "",
            button=False, 
            buttonlabel="",
            width=20,
            command: Optional[Callable[[], None]] = None):
        super().__init__(
            parent,
            background="white",
            bd=0,
            highlightbackground=COLOR.ENTRY_FIELD_HIGHLIGHT,
            highlightthickness=1)
        
        self.field = tk.Entry(
            self,
            bd=0,
            highlightthickness=0,
            width=width)
        
        self.field.pack(
            expand=True,
            fill="both",
            side="left")

        self.button = None

        if button:
            self.button = ButtonFrame(
                self,
                command=command,
                ipadx=4,
                label=buttonlabel,
                style=buttonstyle)
            
            self.button.pack(
                side="right", 
                fill="y")
            