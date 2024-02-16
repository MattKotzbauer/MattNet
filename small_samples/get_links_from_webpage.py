from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
 
req = Request("http://slashdot.org")
html_page = urlopen(req)
 
soup = BeautifulSoup(html_page, "lxml")
 
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
 
print(links)