
#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import sys
import django
django.setup()
from bs4 import BeautifulSoup
import requests
import re
from spider.models import Spider

 
 
def main():
	
    root_url = "http://cse.whu.edu.cn/index.php?s=/home/xwzx/lists/category/tzgg.html"
    root_html  = requests.get(root_url)
    regexString = r'<div class=\"news_list\">((?:(?!<\/div>).)*)<\/div>'
    regexMatch = re.search(regexString, root_html.text, re.DOTALL)
    root_soup = BeautifulSoup(regexMatch.group(0),'html.parser')
    hrefs = root_soup.find_all('a')
    urls =[]
    for href in hrefs:
    	urls.append("http://cse.whu.edu.cn"+href.get('href'))
    for new_url in urls:
        new_html =requests.get(new_url)
        new_soup = BeautifulSoup(new_html.text,'html.parser')
        link1 = new_soup.find_all('div',class_="news_view_t")
        link2 = new_soup.find_all('div',class_="news_view_cs")
        link3 = new_soup.find_all('div',class_="news_view")
        for idx in range(len(link1)):
            title = link1[idx].get_text()
            Spider.objects.create(title=title)
        for idx in range(len(link2)):
            time= link2[idx].get_text()
            Spider.objects.create(time=time)
        for idx in range(len(link3)):
            text= link3[idx].get_text()
            Spider.objects.create(text=text)
    
    
 
if __name__ == "__main__":
    main()
    print('Done!')
