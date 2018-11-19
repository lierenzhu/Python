import requests
from bs4 import BeautifulSoup
import re
import io
import os
import sys
import time
import random

#伪装各种浏览器header
headers0 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}

headers1 = {
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"

}

headers2 = {
    "User-Agent":"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"

}

headers3 = {
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"

}

headers4 = {
    "User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"

}

headers5 = {
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"

}
#将抓取到的标题、正文写入到文件
def wirteFile(name,content):
    file = open("末班车.txt","a+",encoding='utf-8')
    file.write("\n\n"+name)
    file.write(content+"\n")
    file.close()

#判断是否抓取完毕
def isNotEnd(url):
    if url == "https://www.ranwena.com/files/article/84/84953//files/article/84/84953/":
        return 0
    else:
        return 1
#抓取需要的元素

def getItems(url):
    i = random.randint(0,5)

    if i == 0:
        response = requests.get(url=url, headers=headers0)
    elif i == 1:
        response = requests.get(url=url, headers=headers1)
    elif i == 2:
        response = requests.get(url=url, headers=headers2)
    elif i == 3:
        response = requests.get(url=url, headers=headers3)
    elif i == 4:
        response = requests.get(url=url, headers=headers4)
    elif i == 5:
        response = requests.get(url=url, headers=headers5)

    soup = BeautifulSoup(response.text,'html.parser')
    nameClass = soup.select('.bookname')

    for items in nameClass:
        name = items.select('h1')[0].text
        nextChapter = items.select('.bottem1')[0].select('a')[3]['href']

    content = soup.select('#content')[0].text
    content = content.replace(u'\xa0\xa0',u'\n')
    nextChapterUrl = "https://www.ranwena.com/files/article/84/84953/" + nextChapter
    return name,content,nextChapterUrl

#主程序
if os.path.exists('nextUrl.txt') == False:
    url = "https://www.ranwena.com/files/article/84/84953/17328548.html"
    print("未找到上一次爬取的断点，将重新开始爬取...")
    time.sleep(3)
else:
    urlFile = open("nextUrl.txt","r",encoding='utf-8')
    url = urlFile.read()
    urlFile.close()
    print("已找到断点，将继续爬取...")
    time.sleep(3)

while isNotEnd(url):
    name,content,nextChapterUrl = getItems(url)
    wirteFile(name,content)
    url = nextChapterUrl
    urlFile = open("nextUrl.txt","w",encoding='utf-8')
    urlFile.write(url)
    urlFile.close()
    time.sleep(random.random())
    print(name,content,nextChapterUrl)
print("已全部爬取完毕...")
