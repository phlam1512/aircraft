import tkinter as tk
from tkinter import filedialog as fd
from tkinter.ttk import Progressbar
import os
import time

class FileDialogDemo(tk.Tk):

    def __init__(self):
        super().__init__()

        # Create a window of 600x300 and center this on the screen.
        width = 600
        height = 300
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.title("My app")

        # Create a file dialog button.
        #self.button = tk.Button(self, text='Click to Open File')
        #self.button.config(command=lambda filepath='.': self.filehandler(filepath))
        #self.button.pack(fill=tk.X)

        self.button_dict = {"Open File": self.filehandler,
                            "Do Something": self.dosomething,
                            "Save Directory": self.savefile,
                            "Quit": self.destroy}
        
        self.title_text = tk.Label(self, text="My title")
        self.title_text.config(font=("Helvetica bold", 32))
        self.title_text.pack()

        self.button_open = tk.Button(self, width=20, text="Open File", padx=5, pady=5, command=self.filehandler)
        self.button_act = tk.Button(self, width=20, text="Do Something", padx=5, pady=5, command=self.dosomething)
        self.button_save = tk.Button(self, width=20, text="Save", padx=5, pady=5, command=self.savefile)
        self.button_quit = tk.Button(self, width=20, text="Quit", padx=5, pady=5, command=self.destroy)

        self.button_open.pack()
        self.button_act.pack()
        self.button_save.pack()
        self.button_quit.pack()

        self.button_act.config(state="disabled")
        self.button_save.config(state="disabled")

        T = tk.Text(self, width=20, height=5)
        
    def getText(inputText):
        print(inputText.get(1.0,"end-1c"))

    # Callback for the file dialog button.
    def filehandler(self):

        filetypes = [
            ('text files', '*.txt')
        ]

        self.file_reference = fd.askopenfilename(
            parent=self,
            title="Open file",
            filetypes=filetypes
        )
        self.button_open.config(state="disabled")
        self.button_act.config(state="normal")

    def dosomething(self):
        self.pbarlabel = tk.Label(self, text="Please wait")
        self.pbarlabel.place(x=300, y=200, anchor="center")
        self.pbar = Progressbar()
        self.pbar.place(x=300, y=220, width=200, anchor="center")
        with open(self.file_reference, "r") as f:
            self.file_contents = f.read()
        self.pbar.step(99.9)
        self.button_act.config(state="disabled")
        self.button_save.config(state="normal")

    def savefile(self):
        savehere = fd.askdirectory(
            parent=self,
            title="Save file"
        )
        
        savefilename = f"{time.strftime('%Y%m%d-%H%M%S')}_output.txt"
        savefilepath = os.path.join(savehere, savefilename)

        with open(savefilepath, "w") as f:
            f.write(self.file_contents)

        self.button_open.config(state="normal")
        self.button_act.config(state="disabled")
        self.button_save.config(state="disabled")
        self.pbar.destroy()
        self.pbarlabel.destroy()

if __name__ == "__main__":
    file_dialog_demo = FileDialogDemo()
    file_dialog_demo.mainloop()