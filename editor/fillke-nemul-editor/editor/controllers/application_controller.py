from constants import APPLICATION_LABEL

from controllers.menu_bar_controller import MenuBarController
from controllers.status_bar_controller import StatusBarController
from controllers.workspace_controller import WorkspaceController

from models.lexical_resource_model import LexicalResourceModel

from views.menu_bar import MenuBar
from views.application_frame import ApplicationFrame

class ApplicationController:
    def __init__(self, tk):
        self.tk = tk

        self.tk.title(APPLICATION_LABEL.TITLE)
        self.tk.minsize(640, 480)

        self.file = LexicalResourceModel()

        self.menu_bar = MenuBar(tk)
        self.application_frame = ApplicationFrame(tk)

        self.tk.config(menu=self.menu_bar)
        self.application_frame.pack(
            expand=True,
            fill="both")

        self.menu_bar_controller = MenuBarController(
            self,
            self.menu_bar)
        
        self.status_bar_controller = StatusBarController(
            self,
            self.application_frame.status_bar_frame)
        
        self.workspace_controller = WorkspaceController(
            self,
            self.application_frame.workspace_frame)
        