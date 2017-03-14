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
		#local
		# driver = webdriver.PhantomJS(executable_path='./phantomjs.exe')
		#product
		driver = webdriver.PhantomJS(executable_path='/opt/lampp/htdocs/dagou/phantomjs')
		driver.get(url)
		time.sleep(3)
		pageSource = driver.page_source
		bsObj = BeautifulSoup(pageSource, "html.parser")
		driver.close()
	except AttributeError as e:
		return None
	return bsObj

def getBsObjData(city):
	if city['web'] == 1 :
		return getBsObjByWebdriver(city['url'])
	return getBsObj(city['url'])

#2ed. Parse data base on the target info

def parseDataTest(bsObj):
	itemList = bsObj.find("table",{"class":"myGVClass"}).find_all("tr",{"class":"myGVAltRow"})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].text.replace("\n", ""),
			"url":'http://caigou.my.gov.cn/ceinwz/'+item.contents[2].a.attrs["href"],
			"city":'绵阳',
			"start_date":item.contents[3].text.replace("\n", "").replace("[正在进行]", ""),
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

def parseMianyang(bsObj):
	itemList = bsObj.find("table",{"class":"myGVClass"}).find_all("tr",{"class":"myGVAltRow"})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].text.replace("\n", ""),
			"url":'http://caigou.my.gov.cn/ceinwz/'+item.contents[2].a.attrs["href"],
			"city":'绵阳',
			"start_date":item.contents[3].text.replace("\n", "").replace("[正在进行]", ""),
			"end_date":""
		}
		records.append(record)
	return records

def parseChengdu(bsObj):
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

	cur.executemany("INSERT IGNORE INTO items (name,url,city,start_date,end_date) VALUES (%(name)s,%(url)s,%(city)s,%(start_date)s,%(end_date)s)", records)
	cur.connection.commit()
	result = cur.rowcount

	cur.close()
	conn.close()

	return result

#4th. Repeat if neccsess


# bsObj = getBsObjByWebdriver("")

# bsObj = getBsObjByWebdriver("http://v2.dyggzy.com/?id=678")

def scrape(city):
	bsObj = getBsObjData(mianyang)

	if bsObj == None:
		print("Title could not be found")
	else:
		records = eval(city['method'] + '(bsObj)')
		print(storeData(records))





mianyang = {
	'url':'http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=2000&jsgc=&zfcg=0000000&tdjy=&cqjy=&PubDateSort=0&ShowPre=1&CbsZgys=0&zbfs=0&qxxx=0&showqxname=0&NewsShowPre=1&wsjj=0&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=nourl',
	'web': 0,
	'method':'parseMianyang'
}

chengdu = {
	'url':'http://www.cdggzy.com/app1/two/jyxx_zbggmore.jsp',
	'web': 1,
	'method':'parseChengdu'
}

scrape(mianyang)

