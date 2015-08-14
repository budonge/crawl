#coding=utf-8
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re,time,datetime 
fin=open("/mnt/yufan/number","r")
fout=open("/mnt/yufan/number.out","w")
fout1=open("/mnt/yufan/log.txt","a")
n=0
def log(k):	
	hosturl = 'http://www.ebnew.com/businessShow-v-id-'+str(k)+'.html'
	posturl = 'https://cas.ebnew.com/cas/login' 
	cj = cookielib.LWPCookieJar()  
	cookie_support = urllib2.HTTPCookieProcessor(cj)  
	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
	urllib2.install_opener(opener)  
	h = urllib2.urlopen(hosturl) 
	headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',  
           	'Referer' : 'https://cas.ebnew.com/cas/login?service=http://www.ebnew.com/businessShow.view?id='+str(k)}  
	postData = {'authorize' : 'true',  
            	'password' : '******',  
            	'service' : 'https://cas.ebnew.com/cas/login?service=http://www.ebnew.com/businessShow.view?id='+str(k), 
            	'username' : '****' 
            }  
	postData = urllib.urlencode(postData) 
	request = urllib2.Request(posturl, postData, headers)  
	response = urllib2.urlopen(request)  
	text = response.read()
	return text
for line in fin:
	k=line.strip()
	url='http://www.ebnew.com/businessShow-v-id-'+str(k)+'.html'
	try:
		page=urllib2.urlopen(url).read()
		m1=re.search(r'"请登录后查看"',page)
		if m1:
			text=log(k)
		else:
			text=page
		m2=re.search(r'<div id="mainarea">(.*)<!--招标信息推荐-->',text,re.M|re.S)
		if m2:
			print >> fout,k
			print >> fout,"<yufan>"+m2.group()+"</yufan>"
			n+=1
	except:
		continue
t=datetime.datetime.now()
print >> fout1,"%s\t\t%s" % (t,str(n-1)+"条")
