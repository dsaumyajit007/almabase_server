from django.shortcuts import render
from django.shortcuts import get_object_or_404,render,redirect

import json,datetime
from api.models import News
from django.http import HttpResponse
import feedparser,json
# Create your views here.
from urlparse import urlparse
from datetime import datetime
import time

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

from django.views.decorators.csrf import csrf_exempt
#'http://economictimes.indiatimes.com/rssfeedsdefault.cms','

def add_news(request):
	website_urls=['http://rss.cnn.com/rss/edition.rss','https://news.ycombinator.com/rss ','http://economictimes.indiatimes.com/rssfeedsdefault.cms','http://yourstory.com/feed/',]

	#request_recvd = request.POST.get('data')
	for website_url in website_urls:
		parsed_uri = urlparse( website_url )
		domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
		print website_url
		feeds=feedparser.parse(website_url)
		print feeds
		for loop in feeds.entries : 
			print loop.published
			print loop.summary_detail.value
			print domain
			print website_url
			print loop.title
			news = News(time_stamp = json.dumps(list(loop.published_parsed)),website = domain, url = website_url,title = loop.title,content = loop.summary_detail.value)
			news.save()
		

		
	# if len([News.objects.get(link = link)]) == 0 :
		
		
	return redirect('/api/')

def index(request):

	news = News.objects.all()
	c=0
	for news1 in news :
		news[c].time_stamp_parsed = time.strftime("%Y-%m-%d", tuple(json.loads(news1.time_stamp)))
		news[c].content = strip_tags(news[c].content)
		c=c+1
	return render(request,'index.html',{'news' : news})


