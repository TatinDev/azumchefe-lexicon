import tkinter as tk

from constants import MENU_BAR_LABEL

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label=MENU_BAR_LABEL.FILE_NEW)
        self.file_menu.add_command(label=MENU_BAR_LABEL.FILE_OPEN)
        self.file_menu.add_separator()
        self.file_menu.add_command(label=MENU_BAR_LABEL.FILE_SAVE)
        self.file_menu.add_command(label=MENU_BAR_LABEL.FILE_SAVE_AS)
        self.file_menu.add_separator()
        self.file_menu.add_command(label=MENU_BAR_LABEL.FILE_EXIT)

        self.add_cascade(label=MENU_BAR_LABEL.FILE_MENU, menu=self.file_menu)

        self.edit_menu=tk.Menu(self, tearoff=0)
        self.edit_menu.add_command(label=MENU_BAR_LABEL.EDIT_UNDO)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label=MENU_BAR_LABEL.EDIT_COPY)
        self.edit_menu.add_command(label=MENU_BAR_LABEL.EDIT_PASTE)
        self.edit_menu.add_command(label=MENU_BAR_LABEL.EDIT_DELETE)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label=MENU_BAR_LABEL.EDIT_FIND)
        self.edit_menu.add_command(label=MENU_BAR_LABEL.EDIT_GO_TO)

        self.add_cascade(label=MENU_BAR_LABEL.EDIT_MENU, menu=self.edit_menu)

        self.help_menu = tk.Menu(self, tearoff=0)
        self.help_menu.add_command(label=MENU_BAR_LABEL.HELP_VIEW_HELP)
        self.help_menu.add_separator()
        self.help_menu.add_command(label=MENU_BAR_LABEL.HELP_ABOUT)

        self.add_cascade(label=MENU_BAR_LABEL.HELP_MENU, menu=self.help_menu)
        