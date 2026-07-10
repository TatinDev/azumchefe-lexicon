from constants import STATUS_BAR_LABEL

class StatusBarController:
    def __init__(self, application, view):
        self.application = application
        self.view = view

    def set_workplace_entries_count(self, count):
        self.view.workplace_entries_count.config(
            text=f"{count} {STATUS_BAR_LABEL.WORKPLACE_ENTRIES_COUNT}")
        