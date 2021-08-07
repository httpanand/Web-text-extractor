from bs4 import BeautifulSoup
from urllib.request import urlopen

web = input('Input web URL')
page = urlopen(web)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

file_name = "output.txt" #output file name
p = soup.get_text()

file = open(file_name ,"w", encoding="utf-8")
file.write(p)
file.close()

print('File saved in',file_name)