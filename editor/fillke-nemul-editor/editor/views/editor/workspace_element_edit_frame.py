import tkinter as tk

from tkinter import ttk

from views.common.entry_frame import EntryFrame
from views.common.element_tree_view_frame import ElementTreeViewFrame

from constants import WORKSPACE_LABEL, XML_TAG, XML_TAG_ATTRIBUTE

class WorkspaceElementEditFrame(tk.Frame):
    def __init__(self, parent, element, model):
        super().__init__(parent)
        self.model = model

        self.paned_window = tk.PanedWindow(
            self,
            orient="horizontal",
            sashpad=2,
            sashrelief="raised",
            showhandle=False
        )
        self.paned_window.pack(expand=True, fill="both")
        
        self.tree_view_frame = ElementTreeViewFrame(
            self,
            dontiterateover=[XML_TAG.LEXICAL_RESOURCE],
            title=WORKSPACE_LABEL.TREE_VIEW_TITLE,
            width=128
        )
        self.edit_attributes_frame = WorkspaceElementEditAttributesFrame(self)

        self.paned_window.add(self.tree_view_frame)
        self.paned_window.add(self.edit_attributes_frame)

        self.tree_view_frame.tree_view.bind(
            "<<TreeviewSelect>>", 
            self._on_internal_tree_select
        )

        self.tree_view_frame.update_view(element)
        self.edit_attributes_frame.update_view(element)

    def _on_internal_tree_select(self, event):
        element_id = self.tree_view_frame.get_element_id_in_selection()
        if element_id is not None:
            element = self.model.get_element_by_id(element_id)
            self.edit_attributes_frame.update_view(element)

class WorkspaceElementEditAttributesFrame(tk.Frame):
    def __init__(self, parent):
            super().__init__(parent)

            self.title_label = tk.Label(
                self, 
                font=("TkHeadingFont", 12, "bold"), 
                padx=2, 
                pady=4)
            
            self.title_label.pack(anchor="nw", side="top")

            ttk.Separator(self, orient="horizontal").pack(
                fill="x",
                side="top")
            
            self.attributes_frame = tk.Frame(self, padx=4, pady=2)
            self.attributes_frame.pack(expand=True, fill="both", side="top")     
            
            # We provide a ttk.Sizegrip to easily resize the window
            self.sizegrip = ttk.Sizegrip(self)
            self.sizegrip.pack(anchor="se", side="right")      
        
            self.element = None
            self.attribute_entries = {}
            
    def update_view(self, element):
        self.element = element

        for attribute in self.attributes_frame.winfo_children():
            attribute.destroy()
        
        self.attribute_entries.clear()

        if element is None:
            return
        
        self.title_label.config(
            text=f"▶ {XML_TAG.FULL_NAME.get(element.tag, element.tag)}")
        
        # We get our attribute names
        attribute_list = XML_TAG_ATTRIBUTE.TAG_TO_ATTRIBUTE_LIST.get(element.tag)

        # We get out attribute full names
        full_name_attribute_list = getattr(attribute_list, "FULL_NAME", {})
        
        if attribute_list is not None:
            attributes = [
                value for key, value in vars(attribute_list).items()
                if not key.startswith('_') # Ignores internal classes
                and isinstance(value, str) 
                and value != "" 
                and not isinstance(value, dict)] # Ignores FULL_NAME
        else:
            attributes = list(element.attrib.keys())

        for row, attribute_key in enumerate(attributes):
            ttk.Label(
                self.attributes_frame,
                anchor="e",
                text=full_name_attribute_list.get(attribute_key, attribute_key)
            ).grid(
                row=row,
                column=0,
                sticky="e",
                padx=4,
                pady=2
            )
            
            entry = EntryFrame(self.attributes_frame)
            
            attribute_value = element.attrib.get(attribute_key, "")
            entry.field.insert(0, attribute_value)
            
            entry.grid(
                row=row,
                column=1,
                sticky="ew",
                padx=4,
                pady=2
            )
            
            self.attribute_entries[attribute_key] = entry

        self.attributes_frame.columnconfigure(0, weight=0)
        self.attributes_frame.columnconfigure(1, weight=1)