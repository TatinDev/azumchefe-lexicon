import tkinter as tk
from tkinter import ttk

from views.common.entry_frame import EntryFrame
from views.common.element_tree_view_frame import ElementTreeViewFrame
from views.editor.workspace_element_edit_frame import WorkspaceElementEditFrame

from constants import APPLICATION_LABEL, COLOR, WORKSPACE_LABEL, XML_TAG, XML_TAG_ATTRIBUTE

class WorkspaceFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.active_children_windows = {}

        self.tool_bar_frame = WorkspaceToolBarFrame(self)
        self.tool_bar_frame.pack(fill="x", side="top")
        
        ttk.Separator(self, orient="horizontal").pack(fill="x", side="top")

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
            iterateuntil=XML_TAG.ENTRY,
            showstatusheader=True,
            title=WORKSPACE_LABEL.TREE_VIEW_TITLE,
            width=192
        )
        self.element_view_frame = WorkspaceElementViewFrame(self)

    def add_view_frames(self):
        if self.tree_view_frame not in self.paned_window.panes():
            self.paned_window.add(self.tree_view_frame)
        if self.element_view_frame not in self.paned_window.panes():
            self.paned_window.add(self.element_view_frame)

    """
    def forget_view_frames(self):
        if self.tree_view_frame in self.paned_window.panes():
            self.paned_window.forget(self.tree_view_frame)
        if self.element_view_frame in self.paned_window.panes():
            self.paned_window.forget(self.element_view_frame)
    """

    def has_active_children_window(self, id):
        return id in self.active_children_windows
    
    def focus_active_children_window(self, id):
        window = self.active_children_windows[id]

        window.lift()
        window.focus_force()

    def create_editor_window(self, element, element_id, model, close_callback):
        element_edit_window = tk.Toplevel(self)
        element_edit_window.title(
            f"{element.attrib.get(XML_TAG_ATTRIBUTE.ENTRY.TITLE, '')} - {APPLICATION_LABEL.TITLE}")
        element_edit_window.geometry("480x320")
        element_edit_window.minsize(480, 320)

        element_edit_frame = WorkspaceElementEditFrame(
            element_edit_window, 
            element=element, 
            model=model
        )
        element_edit_frame.pack(expand=True, fill="both")
        
        element_edit_window.protocol(
            "WM_DELETE_WINDOW", 
            lambda: close_callback(element_id, element_edit_window)
        )
        
        return element_edit_window

    def destroy_editor_window(self, element_id, window):
        if element_id in self.active_children_windows:
            del self.active_children_windows[element_id]
        window.destroy()

class WorkspaceToolBarFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.search_title = ttk.Label(
            self, 
            text=WORKSPACE_LABEL.TOOL_BAR_SEARCH_TITLE)
        self.search_field = EntryFrame(
            self,
            button=True,
            buttonlabel=WORKSPACE_LABEL.TOOL_BAR_SEARCH_GO_BUTTON,
            buttonstyle="accent",
            width=24)

        self.search_title.pack(padx=8, side="left")
        self.search_field.pack(side="left", pady=4)

class WorkspaceElementViewFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # This is where we save our styles for tk.Text
        self._STYLES = {
            "NORMAL": {
                "font": ("TkDefaultFont", 14)
            },
            "HEADER_1": {
                "font": ("TkHeadingFont", 28, "bold"), 
                "foreground": COLOR.ARTICLE_TITLE_FOREGROUND
            },
            "HEADER_2": {
                "font": ("TkHeadingFont", 18)
            },
            "HEADER_3": {
                "font": ("TkHeadingFont", 16, "bold")
            },
            "HEADER_4": {
                "font": ("TkHeadingFont", 16)
            },
            "SUBHEADER_1": {
                "font": ("TkHeadingFont", 18, "italic")
            },
            "SUBHEADER_2": {
                "font": ("TkDefaultFont", 14, "italic")
            }
        }

        self.content = tk.Text(
            self,
            wrap="word",
            background=COLOR.ARTICLE_BACKGROUND,
            padx=8,
            pady=8,
            borderwidth=1,
            highlightthickness=0,
            width=8,
            height=8,
            cursor="arrow",
            relief="sunken",
            state="disabled")

        self.yscroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.content.yview) 

        self.content.grid(row=0, column=0, sticky="nsew")
        self.yscroll.grid(row=0, column=1, sticky="ns")

    def update_view(self, element, drawuntil):
        if element is None:
            return
        
        # We enable tk.Text to be written on
        self.content.config(state="normal")

        self.content.delete("1.0", tk.END)

        self._draw(element, drawuntil=drawuntil)
        
        # When finished, we disable it
        self.content.config(state="disabled")

    def _draw(self, e, indent=0, drawuntil=""):
        chunks = []

        # We style depending on which XML_TAG and XML_TAG_ATTRIBUTE
        if e.tag in (XML_TAG.LEXICAL_RESOURCE, XML_TAG.ENTRY):
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.LEXICAL_RESOURCE.TITLE):
                chunks.append((val, "HEADER_1"))

        elif e.tag == XML_TAG.FORM:
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.FORM.TITLE):
                chunks.append((f", {val}", "HEADER_2"))
        
        elif e.tag == XML_TAG.SUBENTRY:
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.ENTRY.TITLE):
                chunks.append((f"|| {val}", "HEADER_3"))
        
        elif e.tag == XML_TAG.SENSE:
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.SENSE.PART_OF_SPEECH):
                chunks.append((f"| {val}", "HEADER_4"))
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.SENSE.GEOGRAPHIC_MARK):
                chunks.append((f" {val}", "SUBHEADER_2"))
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.SENSE.CONTEXT_MARK):
                chunks.append((f" {val}", "SUBHEADER_2"))
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.SENSE.EDITORIAL_NOTE):
                chunks.append((f" ({val})", "SUBHEADER_2"))

        elif e.tag == XML_TAG.REFERENCE:
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.REFERENCE.RESOURCE_IDENTIFIER):
                if e.getparent().tag == XML_TAG.SENSE:
                    chunks.append((f"▶ {val}", "HEADER_3"))
                else:
                    chunks.append((f" ({val})", "SUBHEADER_2"))

        elif e.tag == XML_TAG.DEFINITION:
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.DEFINITION.CONTENT):
                chunks.append((f"• {val}", "NORMAL"))
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.DEFINITION.EDITORIAL_NOTE):
                chunks.append((f" ({val})", "SUBHEADER_2"))

        elif e.tag == XML_TAG.QUOTE:
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.QUOTE.CONTENT):
                chunks.append((val, "SUBHEADER_2"))
            if val := e.attrib.get(XML_TAG_ATTRIBUTE.QUOTE.TARGET_LANGUAGE_TRANSLATION):
                chunks.append((f" '{val}'", "SUBHEADER_2"))
        else:
            chunks.append((e.tag, "NORMAL"))

        if chunks:
            indent_tag = f"indent_{indent}"
            self.content.tag_config(
                indent_tag, 
                lmargin1=24 * indent, 
                lmargin2=24 * indent, 
                spacing3=6)
            
            for text, style in chunks:
                if style in self._STYLES:
                    self.content.tag_config(style, **self._STYLES[style])
                
                self.content.insert(tk.END, text, (style, indent_tag))
                
            self.content.insert(tk.END, "\n")

        if e.tag == drawuntil:
            return
        
        for child in e:
            self._draw(child, indent + 1)
            