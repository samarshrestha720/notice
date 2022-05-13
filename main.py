from bs4 import BeautifulSoup
import requests, time

# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("key.json")
# firebase_admin.initialize_app(cred)

count=0
while True:
  data = requests.get(
      "http://nec.edu.np/index.php?                    option=com_content&view=category&id=47&Itemid=74"
  )
  data.raise_for_status()
  
  soup = BeautifulSoup(data.text, 'html.parser')
  
  first = soup.find('tr', {'class': 'sectiontableentry1'})
  title = first.find('a').text.strip()
  link=first.find('a').get('href')
  hits=first.find_all('td')[2].text.strip()
  print("Title: ", title)
  print("Link: http://nec.edu.np"+link)
  print("Hits: ",hits)
  count+=1
  print("count: ",count)
  time.sleep(30)