from bs4 import BeautifulSoup
import requests, time
from keep_alive import keep_alive
import pyshorteners
import re, csv
import os, asyncio,aiohttp


type_bitly = pyshorteners.Shortener(
    api_key='daa876e13a562bea8962a76e506a74bc3d4cb746')  #bitly api key
fbToken = 'EAAMDySMjW2MBAHscR2ifFDdeHLy6Vn1dNa53NHxL5zrcnVhcsyF5qX42ZBYWMAqHGzrhpSPHyeS6YlmflRYaJyZCL5aY4U2IYz1887MuqXwh4qJyKsyeWfFSm7fEd4cg8L1CkQaOsaZBb8a3nOwdEIjxROmnc9Jd9TgAOKZAM9wFVJYEitWgex7wtTPd3RAZD'



#thread = threading.Thread(target=disRun)


def wtofile(title, url, shortUrl):  #write to file function
    with open('notices.csv', mode='a') as wfile:
        rows = [title, url, shortUrl]
        writer = csv.writer(wfile)
        writer.writerow(rows)
        wfile.close()


def sendSms(title, shortUrl):  #send sms function
    msg = f"NEC New Notice:\n{title}\n{shortUrl}\n-NotifyNotice"  #message
    with open('phone.csv', mode='r') as phFile:
        phList = csv.reader(phFile)
        for phno in phList:
            send_url = f"http://api.ininepal.com/api/index?username=inisamarshrestha&password=nepal@123&message={msg}&destination={phno[0]}&sender=SMS"
            print(send_url)
            print(phno[0] + " " + msg)
            response = requests.post(send_url)
            print(response.text)

    phFile.close()


def sendPost():
    msg = f"NEC New Notice:\n{title}\n{url}\n-NotifyNotice"
    send_fb = f"https://graph.facebook.com/101231042826318/feed?message={msg}&access_token={fbToken}"
    response_fb = requests.post(send_fb)
    print(response_fb.text)



def getImg(url):
  data = requests.get(url, verify=False)
  soup = BeautifulSoup(data.text, 'html.parser')
  postContent = soup.find('div', {'class': 'PostContent'})
  imgUrl = postContent.find('img').get('src')
  return imgUrl


keep_alive()  #ping/call uptime robot
count = 0


  
while True:
        data = requests.get(
            "http://nec.edu.np/index.php?option=com_content&view=category&id=47&Itemid=74",
            verify=False)
        data.raise_for_status()
        soup = BeautifulSoup(data.text, 'html.parser')
        first = soup.find('tr', {'class': 'sectiontableentry1'})
        title = first.find('a').text.strip()
        link = first.find('a').get('href')

        with open('notices.csv', mode='r') as file:
            csvFile = csv.reader(file)
            flag = 0
            for lines in csvFile:
                if (lines[0] == title):
                    print('NO NEW NOTICES!!')
                    flag = 1
                    break
            if (flag == 0):
                print('NEW NOTICE ALERT!!')
                print("Title: ", title)
                url = "http://nec.edu.np" + link
                print("Link: " + url)
                shortUrl = re.split("^https://", type_bitly.bitly.short(url))
                #imgUrl = "http://nec.edu.np" + getImg(url)  #get img url
                print("The Shortened URL is: " + shortUrl[1])
                wtofile(title, url, shortUrl[1])
                #sendSms(title, shortUrl[1])  #send sms function
                #sendPost()  #post on page
                                
            file.close()
            count = count + 1
            print("count: ", count)
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
