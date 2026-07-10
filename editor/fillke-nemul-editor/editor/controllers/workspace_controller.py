import os

from constants import APPLICATION_LABEL, XML_TAG

class WorkspaceController:
    def __init__(self, application, view):
        self.application = application
        self.view = view

        self.view.tree_view_frame.tree_view.bind(
            "<<TreeviewSelect>>",
            self.on_tree_node_selected)
        self.view.tree_view_frame.tree_view.bind(
            "<Double-1>",
            self.on_tree_node_double_clicked)

    def open_file(self, path=None):
        if path == "":
            return
        
        self.application.file.open(path)

        if not path:
            path = "Sin título"
        
        self.application.tk.title(
            f"{os.path.basename(path)} - {APPLICATION_LABEL.TITLE}")
        
        self.view.add_view_frames()
        
        self.update_tree_view_frame()
        self.application.status_bar_controller.set_workplace_entries_count(
            self.application.file.get_entries_count())

    def update_tree_view_frame(self):
        root_element = self.application.file.get_root_element()

        self.view.tree_view_frame.update_view(root_element)
    
    def on_tree_node_selected(self, event):
        element_id = self.view.tree_view_frame.get_element_id_in_selection()

        if not element_id:
            return

        element = self.application.file.get_element_by_id(element_id)

        self.view.element_view_frame.update_view(
                element, 
                drawuntil=XML_TAG.LEXICAL_RESOURCE)
        
    def on_tree_node_double_clicked(self, event):
        element_id = self.view.tree_view_frame.get_element_id_in_selection()
        if not element_id:
            return

        if self.view.has_active_children_window(element_id):
            self.view.focus_active_children_window(element_id)
            return
        
        element = self.application.file.get_element_by_id(element_id)
        
        new_window = self.view.create_editor_window(
            element=element,
            element_id=element_id, 
            model=self.application.file,
            close_callback=self.on_edit_window_closed)
        self.view.active_children_windows[element_id] = new_window

    def on_edit_window_closed(self, element_id, window):
        self.view.destroy_editor_window(element_id, window)
        