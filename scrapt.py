from urllib.request import urlopen
from urllib.error import HTTPError
from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
import time
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

def getBsObjByWebdriver(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		driver = webdriver.PhantomJS(executable_path='./phantomjs.exe')
		driver.get(url)
		time.sleep(3)
		pageSource = driver.page_source
		bsObj = BeautifulSoup(pageSource, "html.parser")
		driver.close()
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
			"url":item.contents[2].attrs['href'].replace("..", "http://www.cdggzy.com/app1"),
			"city":'成都'+item.contents[1].text,
			"start_date":item.contents[0].text,
		}
		records.append(record)
	print(records)




def parseData(bsObj):
	itemList = bsObj.find("ul", {"class":"qy_list"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].text,
			"url":item.contents[2].attrs['href'].replace("..", "http://www.cdggzy.com/app1"),
			"city":'成都'+item.contents[1].text,
			"start_date":item.contents[0].text,
			"end_date":""
		}
		records.append(record)
	return records

#3rd. Store data

def storeData(records):
	conn = pymysql.connect(host='127.0.0.1', user='dagou', passwd='v4Qolwc1sMLIXmYO', db='dagou',charset="utf8")

	cur = conn.cursor()
	cur.execute("USE dagou")

	cur.executemany("INSERT INTO items (name,url,city,start_date,end_date) VALUES (%(name)s,%(url)s,%(city)s,%(start_date)s,%(end_date)s)", records)
	cur.connection.commit()

	cur.close()
	conn.close()

#4th. Repeat if neccsess


bsObj = getBsObjByWebdriver("http://www.cdggzy.com/app1/two/jyxx_zbggmore.jsp")

if bsObj == None:
	print("Title could not be found")
else:
	# parseDataTest(bsObj)
	records = parseData(bsObj)
	# print(records)
	storeData(records)