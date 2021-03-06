from tkinter import Tk, ttk, constants

class GUI:
    """Creates and manages user interface"""
    def __init__(self, root, nstring):
        self._root = root
        self._nstring = nstring
        self._entry = None
        self._yes_button = None
        self._header = None

    def create_object(self):
        self._header = ttk.Label(master=self._root, text="Click here to open daily briefing")
        self._entry = ttk.Entry(master=self._root)

        self._yes_button = ttk.Button(master=self._root, text="OK", command=lambda:self._onclick())
        self._yes_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._yes_button.pack(padx=20, pady=20)
        self._header.pack(padx=20, pady=20)


    def _onclick(self):
        self._yes_button.destroy()
        self._header.destroy()

        for i in range(len(self._nstring)):
            title = ttk.Label(master=self._root, text=self._nstring[i]+'\n'*2, wraplength=950)
            title.pack(padx=20, pady=20)

def main_loop(nstring):
    """Main loop for creating and running the UI"""
    window = Tk()
    window.title = ('Daily briefing')
    window.geometry("1000x2000")

    new_ui = GUI(window, nstring)
    new_ui.create_object()

    window.mainloop()
