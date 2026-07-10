import tkinter as tk
from tkinter import ttk

from constants import WORKSPACE_LABEL, COLOR, XML_TAG, XML_TAG_ATTRIBUTE

class ElementTreeViewFrame(tk.Frame):
    def __init__(
            self, 
            parent, 
            dontiterateover=[],
            iterateuntil=None,
            showstatusheader=False,
            title="", 
            width=None):
        super().__init__(
            parent,
            padx=6)
        
        self.dont_iterate_over = dontiterateover
        self.iterate_until = iterateuntil

        self.status = WORKSPACE_LABEL.TREE_VIEW_DEFAULT_STATUS
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=0) 

        self.yscroll = ttk.Scrollbar(self, orient="vertical")

        self.tree_view = ttk.Treeview(
            self,
            columns=(),
            show="tree",
            yscrollcommand=self.yscroll.set)
        
        if width is not None:
            self.tree_view.column("#0", width=width)

        self.status_label = tk.Label(
            self, 
            anchor="w",
            bg=COLOR.TREE_VIEW_STATUS,
            padx=2, 
            text=self.status)

        self.title_label = tk.Label(
            self, 
            anchor="e",
            font=("TkHeadingFont", 12, "bold"), 
            padx=2, 
            pady=2,
            text=title)
        
        self.tree = {}

        self.yscroll.config(command=self.tree_view.yview)

        if showstatusheader:
            self.status_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.tree_view.grid(row=1, column=0, sticky="nsew")
        self.yscroll.grid(row=1, column=1, sticky="ns")

        self.title_label.grid(row=2, column=0, columnspan=2, sticky="ew")

    def get_element_id_in_selection(self):
        selection = self.tree_view.selection()

        if not selection:
            return None
        
        element_id = selection[0]
        return self.tree.get(element_id)
    
    def update_view(self, root_element):
        self.tree_view.delete(*self.tree_view.get_children())
        self.tree.clear()

        if root_element is not None:
            self._insert_node_in_tree("", root_element)

    def _insert_node_in_tree(self, parent, element):
        node_label = ""

        if element.tag == XML_TAG.LEXICAL_RESOURCE:
            node_label = element.attrib.get(
                XML_TAG_ATTRIBUTE.LEXICAL_RESOURCE.TITLE, 'sin título')
        elif element.tag == XML_TAG.ENTRY_GROUP:
            node_label = element.attrib.get(
                XML_TAG_ATTRIBUTE.ENTRY_GROUP.TITLE, 'sin título')
        elif element.tag in (XML_TAG.ENTRY, XML_TAG.SUBENTRY):
            node_label = element.attrib.get(
                XML_TAG_ATTRIBUTE.ENTRY.TITLE, 'sin título')
        elif element.tag == XML_TAG.FORM:
            form_title = element.attrib.get(
                XML_TAG_ATTRIBUTE.FORM.TITLE, 'sin título')
            
            node_label = f"{XML_TAG.FULL_NAME.get(XML_TAG.FORM, '')} ({form_title})"
        else:
            node_label = XML_TAG.FULL_NAME.get(element.tag, element.tag)

        node = self.tree_view.insert(
            parent,
            "end",
            open=True,
            text=node_label)
        
        self.tree[node] = id(element)

        if element.tag == self.iterate_until:
            return

        if element.tag not in self.dont_iterate_over:
            for child in element:
                self._insert_node_in_tree(node, child)
