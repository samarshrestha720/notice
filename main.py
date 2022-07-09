from bs4 import BeautifulSoup
import requests, time
from keep_alive import keep_alive
import datetime as dt
import pyshorteners
import re
import csv


type_bitly = pyshorteners.Shortener(api_key='daa876e13a562bea8962a76e506a74bc3d4cb746') #bitly api key

def wtofile(): #write to file function
  with open('notices.csv', mode='a') as wfile:
          rows = [title,url,shortUrl[1]]
          writer = csv.writer(wfile)
          writer.writerow(rows)
          wfile.close()
    
count=0
keep_alive() #ping/call uptime robot 

while True:
  data = requests.get(
      "http://nec.edu.np/index.php?                    option=com_content&view=category&id=47&Itemid=74", verify=False
  )
  data.raise_for_status()
  soup = BeautifulSoup(data.text, 'html.parser') 
  first = soup.find('tr', {'class': 'sectiontableentry1'})
  title = first.find('a').text.strip()
  link=first.find('a').get('href')
  hits=first.find_all('td')[2].text.strip()
  
  with open('notices.csv', mode='r') as file:
    csvFile = csv.reader(file)
    flag=0
    for lines in csvFile:
      if(lines[0]==title):
        print('NO NEW NOTICES!!')
        flag = 1
        break
    if(flag==0):
      print('NEW NOTICE ALERT!!')
      print("Title: ", title)
      url = "http://nec.edu.np"+link
      print("Link: "+url)
      shortUrl= re.split("^https://",type_bitly.bitly.short(url))
      print("The Shortened URL is: " + shortUrl[1])
      wtofile()
    file.close()
    count+=1
    print("count: ",count)
    time.sleep(60)       






  # print("Title: ", title)
  # print("Link: http://nec.edu.np"+link)
  # print("Hits: ",hits)
  # count+=1
  # print("count: ",count)
  # print(dt.datetime.now())
  # 




#csv:

# fields = ['Title','url','s_url']
# rows = [{'Title': 'Notice : Regular Classes conduction on Friday','url':'https://nec.edu.np/index.php?option=com_content&view=article&id=994:notice-regular-classes-conduction-on-friday&catid=47:notices&Itemid=74'}]
# with open('notices.csv', mode='w') as file:
#   # creating a csv dict writer object
#   writer = csv.DictWriter(file, fieldnames = fields )
#   # writing headers (field names)
#   writer.writeheader()

#   writer.writerows(rows)
  
  