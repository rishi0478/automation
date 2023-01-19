import requests
from bs4 import BeautifulSoup as bs

url = input("Source url :- ")
b = input('Target url :- ')
response = requests.get(url)
soup = bs(response.content,'html.parser')
links = soup.find_all('a')
for link in links:
    href = link['href']
    if href:
      if href == b:
       # print(link['rel'],[href])
         print(link)



        

      