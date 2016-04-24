from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('https://eatatstate.com/menus/brody') as response:
   html = response.read()
   soup = BeautifulSoup(html, 'html.parser')

   print(soup.prettify())
