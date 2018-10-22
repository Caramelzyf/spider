# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import re
def search_form(request):
    return render_to_response('search_form.html')
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            return render(request, 'errors.html')
        else:
            post_list = Spider.objects.filter(title__icontains=q)
            if len(post_list) == 0 :
                return render(request,'search_results.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'search_results.html', {'post_list' : post_list,
                                                    'error' : False})
    return render(request, 'search_results.html', {'post_list': post_list})

def Spider(request):
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
        context          = {}
        for idx in range(len(link1)):
            context['title'] = link1[idx].get_text()

        for idx in range(len(link2)):
            context['time'] = link2[idx].get_text()

        for idx in range(len(link3)):
            context['text'] = link3[idx].get_text()
        
    return render(request, 'spider.html', context)

