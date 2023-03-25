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
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.url_entry = tk.Entry(self.frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        # create output text widget
        self.output_text = tk.Text(self.frame, width=55, height=26)
        self.output_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # create button
        self.scrape_button = tk.Button(
            self.frame, text="Scrape", command=self.scrape, width=10)
        self.scrape_button.grid(row=2, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(
            self.frame, text="Clear", command=self.clear_output, width=10)
        self.clear_button.grid(row=2, column=1, padx=5, pady=5)

    def scrape(self):
        # get URL from entry field
        url = self.url_entry.get()

        # make request to website
        response = requests.get(url)
        html_content = response.content

        # parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # find table element
        table = soup.find('table')

        # create table header
        table_header = []
        for th in table.find_all('th'):
            table_header.append(th.text.strip())

        # create table rows
        table_rows = []
        for tr in table.find_all('tr'):
            table_row = []
            for td in tr.find_all('td'):
                table_row.append(td.text.strip())
            table_rows.append(table_row)

        # display table in output text widget
        self.output_text.delete('1.0', tk.END)
        for header in table_header:
            self.output_text.insert(tk.END, header + '\t')
        self.output_text.insert(tk.END, '\n')
        for row in table_rows:
            for cell in row:
                self.output_text.insert(tk.END, cell + '\t')
            self.output_text.insert(tk.END, '\n')

    def clear_output(self):
        self.output_text.delete("1.0", "end-1c")
