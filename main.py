import tkinter as tk
import requests
from bs4 import BeautifulSoup


class PythonWebScraper:
    def __init__(self, master):
        self.master = master
        master.title("Web Scraper")

        # create labels and entry fields
        self.url_label = tk.Label(master, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)
        self.output_text = tk.Text(master, width=50, height=10)
        self.output_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # create buttons
        self.scrape_button = tk.Button(
            master, text="Scrape", command=self.scrape, width=10)
        self.scrape_button.grid(row=3, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(
            master, text="Clear", command=self.clear_output, width=10)
        self.clear_button.grid(row=3, column=1, padx=5, pady=5)

    def scrape(self):
        # get URL from entry field
        url = self.url_entry.get()

        # make request to website
        response = requests.get(url)
        html_content = response.content

        # parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # find all links on the webpage
        links = soup.find_all('a')

        # clear output text
        self.output_text.delete('1.0', tk.END)

        # output data to text field
        for link in links:
            self.output_text.insert(tk.END, link.get('href') + '\n')

    def clear_output(self):
        self.output_text.delete('1.0', tk.END)


root = tk.Tk()

web_scraper_gui = PythonWebScraper(root)
root.mainloop()
