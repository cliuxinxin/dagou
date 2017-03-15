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

def parseDeyang(bsObj):
	itemList = bsObj.find("div", {"id":"ArticleBox"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].attrs['title'],
			"url":"http://v2.dyggzy.com"+item.contents[2].attrs['href'],
			"city":"德阳",
			"start_date":item.contents[0].text,
			"end_date":''
		}
		records.append(record)
	return records	

def parseShuiling(bsObj):
	itemList = bsObj.find("div", {"class":"box-text-list"}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[7].text,
			"url":item.contents[7].attrs['href'],
			"city":'遂宁',
			"start_date":item.contents[1].text,
			"end_date":''
		}
		records.append(record)
	return records	

def parseNanchong(bsObj):
	itemList = bsObj.find_all("li",{'class':'list-li'})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[1].contents[0].text,
			"url":"http://www.scncggzy.com.cn"+item.contents[1].attrs['href'],
			"city":'南充',
			"start_date":item.contents[1].contents[1].text,
			"end_date":''
		}
		records.append(record)
	return records


def parseGuangyuan(bsObj):
	itemList = bsObj.find('table',{'class':'myGVClass'}).find_all("tr",{'class':'myGVAltRow'})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].a.text,
			"url":"http://www.gyggzy.gov.cn/ceinwz/"+item.contents[2].a.attrs['href'],
			"city":'广元',
			"start_date":'2000-1-1',
			"end_date":''
		}
		records.append(record)
	return records


def parseBazhong(bsObj):
	itemList = bsObj.find('div',{'id':'listCon'}).find_all("li")
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].attrs['title'],
			"url":"http://220.166.21.50:82"+item.contents[2].attrs['href'],
			"city":'巴中',
			"start_date":item.contents[0].text,
			"end_date":''
		}
		records.append(record)
	return records

def parseDazhou(bsObj):
	itemList = bsObj.find_all("tr",{'class':'trfont'})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[3].a.attrs['title'],
			"url":"http://www.dzggzy.cn"+item.contents[3].a.attrs['href'],
			"city":'达州',
			"start_date":item.contents[5].text.replace("[","").replace("]",""),
			"end_date":''
		}
		records.append(record)
	return records

def parseLuzhou(bsObj):
	itemList = bsObj.find('table',{'class':'myGVClass'}).find_all("tr",{'class':'myGVAltRow'})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].a.text,
			"url":"http://ggzy.luzhou.gov.cn/ceinwz/"+item.contents[2].a.attrs['href'],
			"city":'泸州',
			"start_date":item.contents[3].text.strip().replace("[正在进行]",""),
			"end_date":''
		}
		records.append(record)
	return records

def parseLuzhou2(bsObj):
	itemList = bsObj.find('table',{'class':'myGVClass'}).find_all("tr",{'class':'myGVAltRow'})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[2].a.text,
			"url":"http://cg.luzhou.gov.cn/ceinwz/WebInfo_List.aspx?newsid=5001,5006,5011,5016,5021,5026,5031,5036&jsgc=&zfcg=01000000&tdjy=&cqjy=&PubDateSort=0&ShowPre=0&CbsZgys=0&zbfs=0&qxxx=0&showqxname=1&NewsShowPre=1&wsjj=2&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=zfcg",
			"city":'泸州',
			"start_date":time.strftime("%Y-", time.localtime())+item.contents[3].text.strip().replace("[正在进行]",""),
			"end_date":''
		}
		records.append(record)
	return records

def parseYibin(bsObj):
	itemList = bsObj.find_all("tr",{'class':{'js','os'}})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[0],
			"url":item.contents[1],
			"city":'宜宾',
			"start_date":item.contents[2],
			"end_date":''
		}
		records.append(record)
	return records

def parseSichuang(bsObj):
	itemList = bsObj.find_all("tr",{'height':'25'})
	records = []
	for item in itemList:
		record = {
			"name":item.contents[3].a.attrs['title'],
			"url":"http://www.spprec.com" + item.contents[3].a.attrs['href'],
			"city":'四川',
			"start_date":item.contents[5].text.replace("[","").replace("]",""),
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

def insertOrUpdateData(data):
	conn = pymysql.connect(host='127.0.0.1', user='dagou', passwd='v4Qolwc1sMLIXmYO', db='dagou',charset="utf8")

	cur = conn.cursor()
	cur.execute("USE dagou")

	cur.execute("INSERT INTO scraps (name,url,insert_numbers,time) VALUES (%(name)s,%(url)s,%(insert_numbers)s,%(time)s) ON DUPLICATE KEY UPDATE insert_numbers=VALUES(insert_numbers),time=VALUES(time)",data)
	cur.connection.commit()
	result = cur.rowcount

	cur.close()
	conn.close()

	return result

#4th. Repeat if neccsess

#5th. Find the data
def findData(condition):
	conn = pymysql.connect(host='127.0.0.1', user='dagou', passwd='v4Qolwc1sMLIXmYO', db='dagou',charset="utf8")

	cur = conn.cursor()
	cur.execute("USE dagou")

	cur.execute("select *  from items where " + condition)
	cur.connection.commit()
	results = cur.fetchall()

	cur.close()
	conn.close()

	return results

#6th. Update the data
def updateData(data,column):
	conn = pymysql.connect(host='127.0.0.1', user='dagou', passwd='v4Qolwc1sMLIXmYO', db='dagou',charset="utf8")

	cur = conn.cursor()
	cur.execute("USE dagou")

	cur.executemany("update items set start_date = %("+column+")s where id = %(id)s",data)
	cur.connection.commit()

	cur.close()
	conn.close()

#7th. Process the data
def updateGuangyuan():
	condition = "city='广元' and start_date='2000-1-1'"

	results = findData(condition)

	data =[]

	for result in results:
		bsObj = getBsObj(result[2])
		item ={
			"id":result[0],
			"start_date":bsObj.find("span",{"id":"lblWriteDate"}).text
		}
		data.append(item)

	updateData(data,"start_date")


# Scrape Data
def scrape(city):
	bsObj = getBsObjData(city)

	if bsObj == None:
		print("Title could not be found")
	else:
		records = eval(city['method'] + '(bsObj)')
		insert_numbers = storeData(records)
		data = {
			"name":city['name'],
			"url":city['url'],
			"insert_numbers":insert_numbers,
			"time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		}
		insertOrUpdateData(data)
		print(city['name'])

def scrapeTest(city):
	bsObj = getBsObjData(city)

	if bsObj == None:
		print("Title could not be found")
	else:
		records=eval(city['method'] + '(bsObj)')
		for record in records:
			for key,content in record.items():
				print('{}:{}'.format(key,content))




mianyang = {
	'url':'http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=2000&jsgc=&zfcg=0000000&tdjy=&cqjy=&PubDateSort=0&ShowPre=1&CbsZgys=0&zbfs=0&qxxx=0&showqxname=0&NewsShowPre=1&wsjj=0&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=nourl',
	'web': 0,
	'method':'parseMianyang',
	'name':'绵阳'
}

chengdu = {
	'url':'http://www.cdggzy.com/app1/two/jyxx_zbggmore.jsp',
	'web': 1,
	'method':'parseChengdu',
	'name':'成都'
}

mianyang2 = {
	'url':'http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=601&jsgc=&zfcg=0100000&tdjy=&cqjy=&PubDateSort=0&ShowPre=1&CbsZgys=0&zbfs=0&qxxx=0&showqxname=0&NewsShowPre=1&wsjj=0&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=nourl',
	'web': 0,
	'method':'parseMianyang',
	'name':'绵阳2'
}

mianyang3 = {
	'url':'http://egpmall.my.gov.cn/Content/247_1',
	'web': 0,
	'method':'parseMianyang3',
	'name':'绵阳3'
}

ziyang = {
	'url':'http://www.zyjyw.cn/Content/603_1',
	'web': 0,
	'method':'parseZiyang',
	'name':'资阳'
}

yaan = {
	'url':'http://ggzy.yazw.gov.cn:8007/JyWeb/XXGK/JYXYZFCGXXFBList?SubType=2&SubType2=2010&Type=%E9%87%87%E8%B4%AD%E4%BF%A1%E6%81%AF',
	'web': 0,
	'method':'parseYaan',
	'name':'雅安'
}

yaan2 = {
	'url':'http://ggzy.yazw.gov.cn:8007/JyWeb/TradeInfo/JingJiaXinXiList?SubType=50000&SubType2=6010&Type=%E7%AB%9E%E4%BB%B7%E4%BF%A1%E6%81%AF',
	'web': 0,
	'method':'parseYaan2',
	'name':'雅安2'
}

meishan = {
	'url':'http://www.msggzy.org.cn/msweb/gcjs/003002/',
	'web':0,
	'method':'parseMeishan',
	'name':'眉山'
}

meishan2 = {
	'url':'http://www.msggzy.org.cn/msweb//zfcg/005003/MoreInfo.aspx?CategoryNum=005003',
	'web':0,
	'method':'parseMeishan2',
	'name':'眉山2'
}

deyang = {
	'url':'http://v2.dyggzy.com/?id=678',
	'web':1,
	'method':'parseDeyang',
	'name':'德阳'
}

shuiling = {
	'url':'http://www.snjsjy.com/Content/Cloud/29_1_20_0',
	'web':0,
	'method':'parseShuiling',
	'name':'遂宁'
}

shuiling2 = {
	'url':'http://www.snjsjy.com/Content/Cloud/265,268_1_20_0',
	'web':0,
	'method':'parseShuiling',
	'name':'遂宁2'
}

nanchong = {
	'url':'http://www.scncggzy.com.cn/TPFront/front_zfcg/071002/?categoryno=0710&category=071002',
	'web':0,
	'method':'parseNanchong',
	'name':'南充'

}

nanchong2 = {
	'url':'http://www.scncggzy.com.cn/TPFront/front_gcjs/072001/?categoryno=0720&category=072001',
	'web':0,
	'method':'parseNanchong',
	'name':'南充2'
}

guangyuan = {
	'url':'http://www.gyggzy.gov.cn/ceinwz/WebInfo_List.aspx?jsgc=0100000&PubDateSort=0&ShowPre=0&newsid=100&FromUrl=jsgc',
	'web':0,
	'method':'parseGuangyuan',
	'name':'广安'
}

# guangyuan2 = {
# 	'url':'http://www.gyggzy.gov.cn/ceinwz/WebInfo_List.aspx?zfcg=0000000&PubDateSort=0&ShowPre=0&newsid=200&FromUrl=zfcg',
# 	'web':0,
# 	'method':'parseGuangyuan'
# }

bazhong = {
	'url':'http://220.166.21.50:82/Category/More?id=643',
	'web':1,
	'method':'parseBazhong',
	'name':'巴中'
}

bazhong2 = {
	'url':'http://220.166.21.50:82/Category/More?id=646',
	'web':1,
	'method':'parseBazhong',
	'name':'巴中2'
}

dazhou = {
	'url':'http://www.dzggzy.cn/dzsggzy/jyxx/025002/025002001/',
	'web':0,
	'method':'parseDazhou',
	'name':'达州'
}

luzhou = {
	'url':'http://ggzy.luzhou.gov.cn/ceinwz/WebInfo_List.aspx?newsid=0&jsgc=0100000000&zfcg=&tdjy=&cqjy=&PubDateSort=0&ShowPre=0&CbsZgys=0&zbfs=0&qxxx=0&showqxname=0&NewsShowPre=1&wsjj=0&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=jsgc',
	'web':0,
	'method':'parseLuzhou',
	'name':'泸州'
}

luzhou2 = {
	'url':'http://cg.luzhou.gov.cn/ceinwz/WebInfo_List.aspx?newsid=5001,5006,5011,5016,5021,5026,5031,5036&jsgc=&zfcg=01000000&tdjy=&cqjy=&PubDateSort=0&ShowPre=0&CbsZgys=0&zbfs=0&qxxx=0&showqxname=1&NewsShowPre=1&wsjj=2&showCgr=0&ShowOverDate=0&showdate=1&FromUrl=zfcg',
	'web':0,
	'method':'parseLuzhou2',
	'name':'泸州2'
}

yibin = {
	'url':'http://www.ybsggzyjyxxw.com/Jyweb/JYXTXiangMuXinXiList.aspx?type=%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B&subType=130',
	'web':0,
	'method':'parseYibin',
	'name':'宜宾'
}

yibin2 = {
	'url':'http://www.ybsggzyjyxxw.com/ZFCG/Default_ZFCG.aspx',
	'web':0,
	'method':'parseShuiling',
	'name':'宜宾2'
}

sichuang = {
	'url':'http://www.spprec.com/sczw/jyfwpt/005001/005001001/',
	'web':0,
	'method':'parseSichuang',
	'name':'四川'
}

sichuang2 = {
	'url':'http://www.spprec.com/sczw/jyfwpt/005002/005002002/005002002002/',
	'web':0,
	'method':'parseSichuang',
	'name':'四川2'
}









scrape(mianyang)
scrape(mianyang2)
scrape(mianyang3)
scrape(ziyang)
scrape(yaan)
scrape(yaan2)
scrape(meishan)
scrape(meishan2)
scrape(shuiling)
scrape(shuiling2)
scrape(nanchong)
scrape(nanchong2)
scrape(guangyuan)
scrape(luzhou)
scrape(luzhou2)
scrape(sichuang)
scrape(sichuang2)
#web
scrape(bazhong)
scrape(bazhong2)
scrape(deyang)
scrape(chengdu)
# #web
# scrapeTest(yibin)
# 乱码
# scrapeTest(dazhou)
updateGuangyuan()
















