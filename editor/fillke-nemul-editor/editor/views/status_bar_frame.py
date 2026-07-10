from tkinter import ttk

class StatusBarFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.workplace_entries_count = ttk.Label(
            self,
            text="")
        
        # We provide a ttk.Sizegrip to easily resize the window
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.pack(
            anchor="se",
            side="right")
        
        self.workplace_entries_count.pack(
            padx=4,
            side="right")
        