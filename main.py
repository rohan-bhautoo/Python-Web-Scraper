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

        self.options = ["Links", "Headings", "Images",
                        "Paragraphs", "Meta Data", "CSS Files", "Scripts"]
        self.variable = tk.StringVar(master)
        self.variable.set(self.options[0])

        self.output_label = tk.Label(master, text="Options:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)

        self.dropdown = tk.OptionMenu(root, self.variable, *self.options)
        self.dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=2, column=0, padx=5, pady=5)
        self.output_text = tk.Text(master, width=50, height=10)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # create buttons
        self.scrape_button = tk.Button(
            master, text="Scrape", command=self.scrape, width=10)
        self.scrape_button.grid(row=4, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(
            master, text="Clear", command=self.clear_output, width=10)
        self.clear_button.grid(row=4, column=1, padx=5, pady=5)

    def scrape(self):
        # get URL from entry field
        url = self.url_entry.get()

        # get option text
        option = self.variable.get()

        # make request to website
        response = requests.get(url)
        html_content = response.content

        # parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # find all links on the webpage
        links = soup.find_all('a')

        # find all headings on the webpage
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # find all images
        images = soup.find_all('img')

        # find all paragraphs
        paragraphs = soup.find_all('p')

        # scrape the meta data of the webpage
        meta_data = soup.find_all(['meta', 'title'])
        
        # scrape the css_files of the webpage
        css_files = soup.find_all('link', attrs={"rel" : "stylesheet"})
        
        # scrape the scripts of the webpage
        scripts = soup.find_all('script')

        # clear output text
        self.output_text.delete('1.0', tk.END)

        # output data to text field
        if option == self.options[0]:
            for link in links:
                self.output_text.insert(tk.END, link.get('href') + '\n')
        elif option == self.options[1]:
            for heading in headings:
                self.output_text.insert(
                    tk.END, heading.get_text().strip() + '\n')
        elif option == self.options[2]:
            for image in images:
                self.output_text.insert(tk.END, image.get('src') + '\n')
        elif option == self.options[3]:
            for paragraph in paragraphs:
                self.output_text.insert(
                    tk.END, paragraph.get_text().strip() + '\n')
        elif option == self.options[4]:
            for meta in meta_data:
                self.output_text.insert(tk.END, str(meta) + '\n')
        elif option == self.options[5]:
            for css_file in css_files:
                self.output_text.insert(tk.END, str(css_file) + '\n')
        elif option == self.options[6]:
            for script in scripts:
                self.output_text.insert(tk.END, str(script) + '\n')

    def clear_output(self):
        self.output_text.delete('1.0', tk.END)


root = tk.Tk()

web_scraper_gui = PythonWebScraper(root)
root.mainloop()
