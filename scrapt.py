from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pymysql
import re


#1st. Get html though domain
def getBsObj(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
	except AttributeError as e:
		return None
	return bsObj

#2ed. Parse data base on the target info

def parseDataTest(bsObj):
	itemList = bsObj.find("ul", {"class":"qy_list"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].text,
			"url":item.contents[2].attrs['href'],
			"city":'成都'+item.contents[1].text,
			"start_date":item.contents[0].text,
		}
		records.append(record)
	print(bsObj)




def parseData(bsObj):
	itemList = bsObj.find("div", {"class":"ui bidlist"}).find_all("span", {"class":"line"})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[0].attrs['title'],
			"url":'http://www.scbid.com'+item.contents[0].attrs['href'],
			"city":item.contents[1].text,
			"start_date":item.contents[2].attrs['title'],
			"end_date":item.contents[3].attrs['title']
		}
		records.append(record)
	return records

#3rd. Store data

def storeData(records):
	conn = pymysql.connect(host='127.0.0.1', user='dagou', passwd='v4Qolwc1sMLIXmYO', db='dagou',charset="utf8")

	cur = conn.cursor()
	cur.execute("USE dagou")

	cur.executemany("INSERT INTO items (name,url,city,start_date,end_date) VALUES (%(name)s,%(url)s,%(city)s,%(start_date)s,%(start_date)s)", records)
	cur.connection.commit()

	cur.close()
	conn.close()

#4th. Repeat if neccsess


bsObj = getBsObj("http://www.cdggzy.com/app1/two/jyxx_zbggmore.jsp")

if bsObj == None:
	print("Title could not be found")
else:
	parseDataTest(bsObj)
	# records = parseData(bsObj)
	# print(records)
	# storeData(records)