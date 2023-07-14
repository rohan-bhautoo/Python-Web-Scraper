<p align="center">
  <img width="500px" src="https://i.ibb.co/t2QNh4R/Web-Scraping.png" alt="Web-Scraping" border="0">
</p>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-2.7.8-brightgreen.svg" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
</p>

Python Web Scraper is a simple web scraping tool built with Python. It allows you to scrape data from web pages, extract information from HTML elements, save data in text file, download all images, and store table data in a CSV file. The tool provides a user-friendly interface using the Tkinter library.

## Prerequisites

### Python 2.x
```bash
python --version
```

#### Library

##### Requests
Requests allows you to send HTTP/1.1 requests extremely easily.
```bash
pip install requests
```

##### BeautifulSoup
Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
```shell
pip install beautifulsoup4
```

## Installation

### Clone the repository
```bash
https://github.com/rohan-bhautoo/Python-Web-Scraper.git
```

## Usage
To run the Python Web Scraper, execute the following command:
```bash
python main.py
```

The application will open a GUI window where you can enter the URL of the web page you want to scrape. You can select various options such as extracting links, headings, images, paragraphs, meta data, CSS files, and scripts. You can also choose to download images and store the data in a CSV file.

## Code Examples

### Scrape Data from Web Page
```python
import requests
from bs4 import BeautifulSoup

# Make request to website
response = requests.get(url)
html_content = response.content

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find elements and extract data
# ...

# Store data in text file
# ...
```

### Download Images from URL
```python
import requests

url = image.get('src')

# send a GET request to the URL to download the image
response = requests.get(url)

# construct the file name to save the image as
filename = os.path.join(directory, 'image{}'.format(count))

# use os.path.splitext to split the filename into base name and extension
_, extension = os.path.splitext(url)

print(filename)

# save the image to the chosen file path
with open(f'{filename}{extension}', 'wb') as f:
    f.write(response.content)
    count += 1
```

### Extract Table Data from Web Page
```python
from bs4 import BeautifulSoup

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
```

## Limitation
- The Python Web Scraper may not work on web pages with complex JavaScript-based content.
- Some websites may have terms of service or robots.txt that prohibit scraping. Make sure to comply with any legal and ethical requirements.

## Author

👤 **Rohan Bhautoo**

* Github: [@rohan-bhautoo](https://github.com/rohan-bhautoo)
* LinkedIn: [@rohan-bhautoo](https://linkedin.com/in/rohan-bhautoo)

## Show your support

Give a ⭐️ if this project helped you!
