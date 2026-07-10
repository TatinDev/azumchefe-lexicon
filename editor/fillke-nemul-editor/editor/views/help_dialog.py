import tkinter as tk
from tkinter import ttk

from constants import MENU_BAR_LABEL

class HelpDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title(MENU_BAR_LABEL.HELP_VIEW_HELP)
        self.transient(parent)
        self.geometry("520x400")
        self.minsize(400, 300)

        main_frame = ttk.Frame(self, padding=8)
        main_frame.pack(expand=True, fill="both")

        text_frame = ttk.Frame(main_frame)
        text_frame.pack(expand=True, fill="both", pady=(0, 8))

        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)

        help_text = tk.Text(
            text_frame,
            wrap="word",
            padx=8,
            pady=8,
            borderwidth=1,
            relief="sunken",
            font=("TkDefaultFont", 10)
        )

        scrollbar = ttk.Scrollbar(
            text_frame,
            orient="vertical",
            command=help_text.yview
        )
        help_text.config(yscrollcommand=scrollbar.set)

        help_text.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        content = """\
BIENVENIDO AL EDITOR ÑI FILLKE NEMÜL

Este editor permite crear y modificar recursos léxicos en formato XML.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nulla sem, dignissim ac ullamcorper ac, elementum sit amet nibh. Nullam efficitur nunc ut nisl feugiat, non laoreet nibh malesuada. Sed at justo quam. Suspendisse luctus molestie diam a aliquet. Ut fermentum varius leo. Duis vitae dui enim. Pellentesque sapien nunc, semper non mi non, consequat lobortis quam. Vestibulum vel egestas nulla, sed faucibus massa. Phasellus accumsan leo eu erat finibus, id faucibus arcu scelerisque. Mauris cursus nec eros at varius. Aliquam erat volutpat. Cras malesuada mauris ligula, sed laoreet nulla volutpat in. Aliquam consectetur rutrum ante non suscipit. Nulla neque enim, euismod in purus sed, pellentesque sagittis massa. Nulla porta tristique tellus, non laoreet augue mollis quis. Sed at diam ac turpis elementum viverra nec vel ipsum.

Nulla vitae ultricies nibh. Nulla facilisi. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer ultrices ipsum in nibh facilisis, ac congue nisi varius. Cras nulla libero, finibus vel velit quis, blandit feugiat tortor. Suspendisse sit amet finibus tortor, id fringilla ligula. Cras venenatis quis arcu malesuada vehicula. Nulla ut metus ante. Fusce porttitor ex non risus hendrerit, id sollicitudin justo aliquam. Ut ultrices ultricies erat, non luctus libero mattis a. Suspendisse placerat tristique malesuada. Nam suscipit laoreet diam, non vulputate velit dignissim non. Sed purus libero, fringilla ut lectus eu, aliquam hendrerit turpis. In sagittis tristique eros, non ultrices mi ornare non. Suspendisse varius eros in porta tempor.

Quisque fermentum sit amet risus ut rhoncus. In venenatis sapien et mattis vehicula. Praesent in tempor risus, in efficitur ligula. Cras et lacus dictum, vestibulum lectus eget, convallis orci. Nulla convallis tellus id congue consequat. Cras ultricies nunc vel odio ultrices, in rhoncus dui posuere. Morbi efficitur nibh id consequat molestie. Pellentesque nec euismod lectus. Nunc luctus lacus vitae aliquam sagittis.

Nulla pulvinar at massa eget lacinia. Nam at urna condimentum, vestibulum quam ac, blandit justo. In suscipit pretium sollicitudin. Duis a dolor non lectus feugiat luctus non eget quam. Vivamus dui dui, tempus a vestibulum non, sagittis in neque. Aliquam imperdiet lacus sed tincidunt mattis. Ut congue dui at purus feugiat, vitae vehicula ligula imperdiet. In vulputate nec mi eget gravida. Quisque vitae tincidunt erat. Vivamus suscipit ex sed libero dictum, vel euismod magna consequat. Vivamus ut posuere turpis.

Vestibulum at sollicitudin velit. Curabitur quis interdum justo, sit amet aliquet sapien. Mauris laoreet ante ac orci aliquam, ac varius sem blandit. Vivamus at nulla dictum, facilisis est vel, pharetra nisl. Maecenas dapibus ipsum vitae porttitor dignissim. Curabitur vitae diam leo. Curabitur egestas tincidunt neque, non suscipit neque posuere in. Suspendisse vulputate augue sit amet metus imperdiet mattis ac eu felis. Vivamus est nisi, dapibus id tincidunt in, tristique sed urna. Nulla facilisi. Vivamus venenatis, quam quis mollis condimentum, mi dolor condimentum orci, ut cursus ligula justo et risus. Etiam elementum diam ut nibh vehicula aliquet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam eleifend turpis eget turpis egestas, eu porttitor massa tempus. Sed eleifend magna felis, a pretium eros interdum sed.
"""
        help_text.insert("1.0", content)
        help_text.config(state="disabled")

        ttk.Button(
            main_frame,
            text="Cerrar",
            command=self.destroy
        ).pack()
