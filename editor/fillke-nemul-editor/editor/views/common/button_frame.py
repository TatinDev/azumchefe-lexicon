import tkinter as tk

from typing import Callable, Literal, Optional

from constants import COLOR

class ButtonFrame(tk.Frame):
    def __init__(
            self, 
            parent, 
            style: Literal['', 'accent'] = "",
            ipadx=1,
            ipady=1,
            highlightthickness=0, 
            fontsize=9, 
            label="",
            command: Optional[Callable[[], None]] = None):
        super().__init__(
            parent,
            bd=0,
            highlightbackground=COLOR.BUTTON_HIGHLIGHT,
            highlightthickness=highlightthickness)
        
        self.style = style
        self.command = command
        self._is_held = False
        
        self.button = tk.Label(
            self,
            bg=COLOR.BUTTON,
            fg=COLOR.BUTTON_HIGHLIGHT,
            font=("TkDefaultFont", fontsize),
            text=label,
            padx=ipadx,
            pady=ipady)
        
        self.button.pack(fill="both")

        # Style defines colours
        if style == "accent":
            self.config(highlightbackground="black")

            self.button.config(
                bg=COLOR.ACCENT_BUTTON, 
                fg="black", 
                font=("TkDefaultFont", fontsize, "bold"))

        self.button.bind("<Enter>", self._on_button_hover)
        self.button.bind("<Leave>", self._on_button_leave)

        self.button.bind("<ButtonPress-1>", self._on_button_hold)
        self.button.bind("<ButtonRelease-1>", self._on_button_release)

    def set_command(self, command):
        self.command = command

    def _on_button_hover(self, event):
        if self.style == "accent":
            self.button.config(bg=COLOR.ACCENT_BUTTON_HOVER)
            self.button.config(fg=COLOR.ACCENT_BUTTON_HOVER_FOREGROUND)
        else:
            self.config(highlightbackground=COLOR.BUTTON_HIGHLIGHT_HOVER)

            self.button.config(fg=COLOR.BUTTON_HIGHLIGHT_HOVER)

    def _on_button_hold(self, event):
        self._is_held = True

        if self.style == "accent":
            self.button.config(fg="black")
        else:
            self.config(highlightbackground=COLOR.BUTTON_HIGHLIGHT_HOLD)

            self.button.config(fg=COLOR.BUTTON_HIGHLIGHT_HOLD)

    def _on_button_release(self, event):
        if self._is_held:
            self._is_held = False

            self._on_button_hover(event)

            if self.command:
                self.command()
            
    def _on_button_leave(self, event):
        self._is_held = False

        if self.style == "accent":
            self.button.config(bg=COLOR.ACCENT_BUTTON)

            self.button.config(fg="black")
        else:
            self.config(highlightbackground=COLOR.BUTTON_HIGHLIGHT)

            self.button.config(fg=COLOR.BUTTON_HIGHLIGHT)
