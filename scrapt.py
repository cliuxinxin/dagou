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

def parseMianyang3(bsObj):
	itemList = bsObj.find("div", {"class":"box-text-list"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[6].text,
			"url":"http://egpmall.my.gov.cn"+item.contents[6].attrs['href'],
			"city":"绵阳竞价",
			"start_date":item.contents[0].text,
			"end_date":""
		}
		records.append(record)
	return records

def parseZiyang(bsObj):
	itemList = bsObj.find("div", {"class":"box-text-list"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[6].text,
			"url":"http://www.zyjyw.cn"+item.contents[6].attrs['href'],
			"city":"资阳",
			"start_date":item.contents[0].text,
			"end_date":""
		}
		records.append(record)
	return records

def parseYaan(bsObj):
	itemList = bsObj.find("div", {"class":"new_news_content"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[1].contents[0].text,
			"url":item.contents[1].attrs['href'],
			"city":"雅安",
			"start_date":item.contents[4].text,
			"end_date":''
		}
		records.append(record)
	return records

def parseYaan2(bsObj):
	itemList = bsObj.find("div", {"class":"new_news_content"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[1].attrs["title"],
			"url":"http://ggzy.yazw.gov.cn:8007"+item.contents[1].attrs["href"],
			"city":"雅安",
			"start_date":item.contents[5].text,
			"end_date":""
		}
		records.append(record)
	return records

def parseMeishan(bsObj):
	itemList = bsObj.find("table", {"width":"99%"}).find_all("tr",{"height":"22"})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[4].contents[0].attrs["title"],
			"url":"http://www.msggzy.org.cn"+item.contents[4].contents[0].attrs["href"],
			"city":"眉山",
			"start_date":item.contents[6].text,
			"end_date":item.contents[8].text
		}
		records.append(record)
	return records

def parseMeishan2(bsObj):
	itemList = bsObj.find("table", {"id":"MoreInfoList1_DataGrid1"}).find_all("tr")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].a.attrs['title'],
			"url":"http://www.msggzy.org.cn"+item.contents[2].a.attrs['href'],
			"city":"眉山",
			"start_date":item.contents[3].text.strip().replace("\r\n", ""),
			"end_date":''
		}
		records.append(record)
	return records



#3rd. Store datas

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
	bsObj = getBsObjData(city)

	if bsObj == None:
		print("Title could not be found")
	else:
		# eval(city['method'] + '(bsObj)')
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

mianyang2 = {
	'url':'http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=601&jsgc=&zfcg=0100000&tdjy=&cqjy=&PubDateSort=0&ShowPre=1&CbsZgys=0&zbfs=0&qxxx=0&showqxname=0&NewsShowPre=1&wsjj=0&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=nourl',
	'web': 0,
	'method':'parseMianyang'
}

mianyang3 = {
	'url':'http://egpmall.my.gov.cn/Content/247_1',
	'web': 0,
	'method':'parseMianyang3'
}

ziyang = {
	'url':'http://www.zyjyw.cn/Content/603_1',
	'web': 0,
	'method':'parseZiyang'
}

yaan = {
	'url':'http://ggzy.yazw.gov.cn:8007/JyWeb/XXGK/JYXYZFCGXXFBList?SubType=2&SubType2=2010&Type=%E9%87%87%E8%B4%AD%E4%BF%A1%E6%81%AF',
	'web': 0,
	'method':'parseYaan'
}

yaan2 = {
	'url':'http://ggzy.yazw.gov.cn:8007/JyWeb/TradeInfo/JingJiaXinXiList?SubType=50000&SubType2=6010&Type=%E7%AB%9E%E4%BB%B7%E4%BF%A1%E6%81%AF',
	'web': 0,
	'method':'parseYaan2'
}

meishan = {
	'url':'http://www.msggzy.org.cn/msweb/gcjs/003002/',
	'web':0,
	'method':'parseMeishan'
}

meishan2 = {
	'url':'http://www.msggzy.org.cn/msweb//zfcg/005003/MoreInfo.aspx?CategoryNum=005003',
	'web':0,
	'method':'parseMeishan2'
}

# scrape(mianyang)
# scrape(mianyang2)
# scrape(mianyang3)
# scrape(chengdu)
# scrape(ziyang)
# scrape(yaan)
# scrape(yaan2)
# scrape(meishan)
scrape(meishan2)





