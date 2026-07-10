import tkinter as tk
from tkinter import ttk

class SearchSuggestionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self._items = []

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.listbox = tk.Listbox(
            self,
            height=5,
            activestyle="none",
            borderwidth=1,
            relief="sunken",
            font=("TkDefaultFont", 10),
            exportselection=False
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.listbox.yview
        )
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.listbox.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    def update_items(self, items):
        self._items = items
        self.listbox.delete(0, tk.END)
        for element_id, label in items:
            self.listbox.insert(tk.END, label)

    def get_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            return None
        index = selection[0]
        if index < len(self._items):
            return self._items[index][0]
        return None

    def get_items(self):
        return self._items
