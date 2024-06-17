import requests
from bs4 import BeautifulSoup
 
c= input("Enter the city name : ")
url = "https://www.google.com/search?q="+"weather"+c
htmlfile = requests.get(url).content
sp = BeautifulSoup(htmlfile , 'html.parser')
temp = sp.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = sp.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
d = str.split('\n')
t = d[0]
s = d[1]
ldiv = sp.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = ldiv[5].text
pos = strd.find('Wind')
o_d = strd[pos:]
print("Temperature is", temp)
print("Time: ", t)
print("Sky Description: ", s)
print(o_d)