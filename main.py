import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import SeleniumURLLoader
from requests_html import HTMLSession
session = HTMLSession()

url = 'https://www.boe.es/biblioteca_juridica/codigos/codigo.php?id=49&modo=2&nota=0&tab=2'
"""urls = ['https://www.boe.es/biblioteca_juridica/codigos/codigo.php?id=49&modo=2&nota=0&tab=2']

print(data)"""

res = session.get(url)
#print(res.text)
soup = BeautifulSoup(res.content,"html.parser")
lst = soup.find_all('ol',class_="noType")
urls = []
base_url = "https://www.boe.es/"
for i in lst:
    a_tag = i.find_all('a')
    for  link in a_tag:
        complete_url = base_url + link["href"]
        urls.append(complete_url)
loader = SeleniumURLLoader(urls=urls)
data = loader.load()
print(data)