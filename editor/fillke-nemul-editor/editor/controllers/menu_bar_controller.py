from tkinter import filedialog

from constants import MENU_BAR_LABEL, WORKSPACE_LABEL

from views.about_dialog import AboutDialog
from views.help_dialog import HelpDialog

class MenuBarController:
    def __init__(self, application, view):
        self.application = application
        self.view = view

        self.view.file_menu.entryconfig(
            MENU_BAR_LABEL.FILE_NEW,
            command=self.new_file)

        self.view.file_menu.entryconfig(
            MENU_BAR_LABEL.FILE_OPEN,
            command=self.open_file)

        self.view.help_menu.entryconfig(
            MENU_BAR_LABEL.HELP_VIEW_HELP,
            command=self.show_help)

        self.view.help_menu.entryconfig(
            MENU_BAR_LABEL.HELP_ABOUT,
            command=self.show_about)

    def new_file(self):
        self.application.workspace_controller.open_file()

    def open_file(self):
        self.application.workspace_controller.open_file(
            filedialog.askopenfilename(title=WORKSPACE_LABEL.DIALOG_FILE_OPEN_TITLE))

    def show_about(self):
        AboutDialog(self.application.tk)

    def show_help(self):
        HelpDialog(self.application.tk)
        