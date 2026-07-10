import tkinter as tk

from controllers.application_controller import ApplicationController

if __name__ == "__main__":
    tk = tk.Tk()

    application_controller = ApplicationController(tk)

    tk.mainloop()