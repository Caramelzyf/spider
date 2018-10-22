
from bs4 import BeautifulSoup
import requests
import re

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
        print(title)
    for idx in range(len(link2)):
        time= link2[idx].get_text()
        print(time)
    for idx in range(len(link3)):
        text= link3[idx].get_text()
        print(text)
