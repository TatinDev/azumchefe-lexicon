from tkinter import ttk

from views.status_bar_frame import StatusBarFrame
from views.workspace_frame import WorkspaceFrame

class ApplicationFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.status_bar_frame = StatusBarFrame(self)
        self.workspace_frame = WorkspaceFrame(self)

        self.workspace_frame.pack(
            expand=True,
            fill="both")
        
        ttk.Separator(self, orient="horizontal").pack(
            fill="x",
            side="top")

        self.status_bar_frame.pack(
            fill="both",
            side="bottom")      
        