import requests
from bs4 import BeautifulSoup

# make a request to the website and retrieve the HTML content
url = 'https://realpython.github.io/fake-jobs/'
response = requests.get(url)
html_content = response.content

# parse HTML Content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# find all links on the webpage
links = soup.find_all('a')

# find all headings on the webpage
headings = soup.find_all(['h1', 'h2', 'h3'])

# find all links that have the text "click here"
links = soup.find_all('a', string='click here')

# find all images that have the class "thumbnail"
images = soup.find_all('img', class_='thumbnail')

# extract all link URLs and store them in a list
link_urls = [link.get('href') for link in links]

# extract all heading text and store them in a list
heading_text = [heading.get_text() for heading in headings]

print(images)