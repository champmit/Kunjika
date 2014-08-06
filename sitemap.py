#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib2

page = urllib2.urlopen("http://localhost:5000").read()

soup = BeautifulSoup(page)
urls = []
for a in soup.findAll('a', href=True):
    #print a['href']
    if a['href'] != '#' and a['href'] not in urls and a['href'] != 'http://libreprogramming.org':
        urls.append(a['href'])

for i in urls:
    #print i
    try:
        page = urllib2.urlopen("http://localhost:5000" + i).read()
        soup = BeautifulSoup(page)
    except:
        pass

    for a in soup.findAll('a', href=True):
        if a['href'] != '#' and a['href'] not in urls and a['href'] != 'http://libreprogramming.org':
            urls.append(a['href'])

print len(urls)

file = open('sitemap.xml', 'w')

file.write('<?xml version="1.0" encoding="UTF-8"?>\n \
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n \
            xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"\n \
            xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n')

for i in urls:
    file.write('<url>\n')
    file.write('\t<loc>' + 'https://kunjika.libreprogramming.org' + i  + '</loc>\n')
    file.write('</url>\n')

file.write('</urlset>')
file.close()