import tkinter as tk
from tkinter import ttk
from scraper import Tab1
from table_data import Tab2


class PythonWebScraper:
    def __init__(self, master):
        self.master = master
        master.title("Web Scraper")

        # create tab control
        self.tabControl = ttk.Notebook(master)
        self.tab1 = Tab1(self.tabControl)
        self.tab2 = Tab2(self.tabControl)
        self.tabControl.add(self.tab1.frame, text='Scraper')
        self.tabControl.add(self.tab2.frame, text='Table Data')
        self.tabControl.pack(expand=True, fill="both")


root = tk.Tk()

web_scraper_gui = PythonWebScraper(root)
root.mainloop()
