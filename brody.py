from bs4 import BeautifulSoup
import urllib.request

dish_list = []

with urllib.request.urlopen('https://eatatstate.com/menus/brody') as response:
   html = response.read()
   soup = BeautifulSoup(html, 'html.parser')
   menuItems = soup.find_all(class_="field-item")
   for item in menuItems:
       dish_list.append(str(item.string))

   print(dish_list)
