from bs4 import BeautifulSoup
import json, time
from datetime import datetime

soup = BeautifulSoup(open("messages.html", encoding="utf8"), 'lxml').body.contents[1]

def getTime(string_time):
    return datetime.fromtimestamp(time.mktime(time.strptime(string_time[:-3], "%A, %B %d, %Y at %I:%M%p ")))

json.dump([{'user': message.find('span', {'class':"user"}).string, 'date': getTime(message.find('span', {'class':"meta"}).string).timestamp(), 'message': message.next_sibling.string} for message in soup.find_all('div', {'class':"message"})], open("messages.json", 'w+'))
