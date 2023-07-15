import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


class Tab2:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)

        # create labels and entry fields
        self.url_label = tk.Label(self.frame, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.url_entry = tk.Entry(self.frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        # store data in CSV checkbox
        self.checkVariable = tk.IntVar(self.frame)
        self.checkbox = tk.Checkbutton(
            self.frame,
            text="Store data in CSV file",
            variable=self.checkVariable,
            onvalue=1,
            offvalue=0,
            command=self.show_hide_checkbox,
        )
        self.checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # include header checkbox
        self.includeHeader = tk.IntVar(self.frame)
        self.csvHeader = tk.Checkbutton(
            self.frame,
            text="Include header in CSV",
            variable=self.includeHeader,
            onvalue=1,
            offvalue=0,
        )
        self.csvHeader.grid_remove()

        # create output table
        self.treeview = ttk.Treeview(self.frame, columns=(), height=20)
        self.treeview.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW
        )

        # create button
        self.scrape_button = tk.Button(
            self.frame, text="Scrape", command=self.scrape, width=10
        )
        self.scrape_button.grid(row=4, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(
            self.frame, text="Clear", command=self.clear_output, width=10
        )
        self.clear_button.grid(row=4, column=1, padx=5, pady=5)

    def scrape(self):
        # get URL from entry field
        url = self.url_entry.get()

        # get checkbox state
        checked = self.checkVariable.get()

        # get includeHeader checkbox state
        includeHeader = self.includeHeader.get()

        # make request to website
        response = requests.get(url)
        html_content = response.content

        # parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # find table element
        table = soup.find("table")

        # create table header
        table_header = []
        for th in table.find_all("th"):
            table_header.append(th.text.strip())

        # create table rows
        table_rows = []
        for tr in table.find_all("tr"):
            table_row = []
            for td in tr.find_all("td"):
                table_row.append(td.text.strip())
            table_rows.append(table_row)

        # clear table
        self.treeview.delete(*self.treeview.get_children())

        # populate table in treeview widget
        self.treeview["columns"] = table_header
        self.treeview["show"] = "headings"
        for header in table_header:
            self.treeview.heading(header, text=header)
            self.treeview.column(header)
        for row in table_rows:
            self.treeview.insert("", tk.END, values=row)

        if checked == 1:
            now = datetime.utcnow()
            format = now.strftime("%Y%m%d%H%M")
            with open(f"csv/csv_{format}.csv", "w") as f:
                csvwriter = csv.writer(f, delimiter=",")

                if includeHeader == 1:
                    print("save header:", table_header)
                    csvwriter.writerow(table_header)

                for row_id in self.treeview.get_children():
                    row = self.treeview.item(row_id)["values"]
                    if row != "":
                        print("save row:", row)
                        csvwriter.writerow(row)

    def clear_output(self):
        self.treeview.delete(*self.treeview.get_children())

    # function to show/hide checkbox based on entry value
    def show_hide_checkbox(self, _=None):
        value = self.checkVariable.get()
        if value == 1:
            self.csvHeader.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        else:
            self.includeHeader.set(0)
            self.csvHeader.grid_remove()
