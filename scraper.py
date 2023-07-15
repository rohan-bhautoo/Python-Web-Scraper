import os
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Tab1:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)

        # create labels and entry fields
        self.url_label = tk.Label(self.frame, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.url_entry = tk.Entry(self.frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        # dropdown options
        self.options = [
            "Links",
            "Headings",
            "Images",
            "Paragraphs",
            "Meta Data",
            "CSS Files",
            "Scripts",
        ]
        self.variable = tk.StringVar(self.frame)
        self.variable.set(self.options[0])
        self.output_label = tk.Label(self.frame, text="Options:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.dropdown = tk.OptionMenu(
            self.frame, self.variable, *self.options, command=self.show_hide_checkbox
        )
        self.dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # download images checkbox
        self.downloadImg = tk.IntVar(self.frame)
        self.checkbox1 = tk.Checkbutton(
            self.frame,
            text="Download images",
            variable=self.downloadImg,
            onvalue=1,
            offvalue=0,
        )
        self.checkbox1.grid_remove()

        # store data in file checkbox
        self.checkVariable = tk.IntVar(self.frame)
        self.checkbox2 = tk.Checkbutton(
            self.frame,
            text="Store data in text file",
            variable=self.checkVariable,
            onvalue=1,
            offvalue=0,
        )
        self.checkbox2.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.output_label = tk.Label(self.frame, text="Output:")
        self.output_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.output_text = tk.Text(self.frame, width=55, height=20)
        self.output_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # create buttons
        self.scrape_button = tk.Button(
            self.frame, text="Scrape", command=self.scrape, width=10
        )
        self.scrape_button.grid(row=6, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(
            self.frame, text="Clear", command=self.clear_output, width=10
        )
        self.clear_button.grid(row=6, column=1, padx=5, pady=5)

    def scrape(self):
        # get URL from entry field
        url = self.url_entry.get()

        # get option text
        option = self.variable.get()

        # get checkbox state
        checked = self.checkVariable.get()

        # get download img checkbox state
        checkedImg = self.downloadImg.get()

        # make request to website
        response = requests.get(url)
        html_content = response.content

        # parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # find all links on the webpage
        links = soup.find_all("a")

        # find all headings on the webpage
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        # find all images
        images = soup.find_all("img")

        # find all paragraphs
        paragraphs = soup.find_all("p")

        # scrape the meta data of the webpage
        meta_data = soup.find_all(["meta", "title"])

        # scrape the css_files of the webpage
        css_files = soup.find_all("link", attrs={"rel": "stylesheet"})

        # scrape the scripts of the webpage
        scripts = soup.find_all("script")

        # clear output text
        self.output_text.delete("1.0", tk.END)

        # output data to text field
        if option == self.options[0]:
            for link in links:
                self.output_text.insert(tk.END, link.get("href") + "\n")
        elif option == self.options[1]:
            for heading in headings:
                self.output_text.insert(tk.END, heading.get_text().strip() + "\n")
        elif option == self.options[2]:
            for image in images:
                self.output_text.insert(tk.END, image.get("src") + "\n")
        elif option == self.options[3]:
            for paragraph in paragraphs:
                self.output_text.insert(tk.END, paragraph.get_text().strip() + "\n")
        elif option == self.options[4]:
            for meta in meta_data:
                self.output_text.insert(tk.END, str(meta) + "\n")
        elif option == self.options[5]:
            for css_file in css_files:
                self.output_text.insert(tk.END, str(css_file) + "\n")
        elif option == self.options[6]:
            for script in scripts:
                self.output_text.insert(tk.END, str(script) + "\n")

        if checked == 1:
            now = datetime.utcnow()
            format = now.strftime("%Y%m%d%H%M")
            with open(f"data/data_{format}.txt", "w") as f:
                f.write(self.output_text.get("1.0", "end-1c"))

        if checkedImg == 1:
            count = 1
            now = datetime.utcnow()
            format = now.strftime("%Y%m%d%H%M")

            directory = "images/" + str(format) + "/"

            # create the directory if it doesn't already exist
            if not os.path.exists(directory):
                os.makedirs(directory)

            # loop through each image and download it
            for image in images:
                url = image.get("src")

                # send a GET request to the URL to download the image
                response = requests.get(url)

                # construct the file name to save the image as
                filename = os.path.join(directory, "image{}".format(count))

                # use os.path.splitext to split the filename into base name and extension
                _, extension = os.path.splitext(url)

                print(filename)

                # save the image to the chosen file path
                with open(f"{filename}{extension}", "wb") as f:
                    f.write(response.content)
                    count += 1

    def clear_output(self):
        self.output_text.delete("1.0", "end-1c")

    # function to show/hide checkbox based on entry value
    def show_hide_checkbox(self, _=None):
        value = self.variable.get()
        if value == self.options[2]:
            self.checkbox1.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        else:
            self.downloadImg.set(0)
            self.checkbox1.grid_remove()
