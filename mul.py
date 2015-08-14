#encoding=utf-8
import multiprocessing
from multiprocessing import Process,Queue,Pool
import  re,urllib2,time,datetime
#fin=open("history","r")#本次抓取前历史链接，用于去重
#fout1=open("today","w")#今天抓取的链接情况
#fout=open("now","w")#本次抓取后的链接,用于下次去重
global count=0
global dict1={}
for line in fin:
	k=line.strip().split('\t')
	dict1[k[0]]=int(k[1])
#往队列中写入网址
def write(q):
	t=datetime.datetime.now()
	y=t.year
	m=t.month
	d=t.day
	str_time=str(y)+"-"+str(m)+"-"+str(d)
	count=0
	for i in range(1,101):#循环终点固定页数（持续抓取）,对于这里可以结合while+正则
#		url="http://www.ebnew.com/tradingIndex.view?key=&pubDateBegin="+str_time+"&pubDateEnd="+str_time+"&infoType=&fundSourceCodes=&zone=&normIndustry=&bidModel=&timeType=custom&sortMethod=&currentPage="+str(i)+"&length=150"
		try:
			req=urllib2.Request(url)
			req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0')
			html=urllib2.urlopen(req)
			page=html.read()
#			list1=re.findall(r'http://www.ebnew.com/businessShow-v-id-(.*).html',page)
			for k in list1:
				print k
				if(not dict1.has_key(k)):
					q.put(k)
					dict1[k]=1
				else:
					dict1[k]+=1
		except:
			continue
#从队列中得到网址，根据网址获取内容，并解析
def read(q):
	while True:
		if not q.empty():
			value=q.get(True)
#			url='http://www.ebnew.com/businessShow-v-id-'+str(value)+'.html'
			try:
				req=urllib2.Request(url)
				req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0')
				html=urllib2.urlopen(req)
				page=html.read()
			#此处代码处理需要登陆
			#此处代码为字段解析功能
			#此处代码还需统计功能
				count+=1
				print count
			except:
				q.put(value) #将无法获取的链接捕获出来put进队列
		else:
			break
if __name__=='__main__':
	manager=multiprocessing.Manager()
	q=manager.Queue()
	p=Pool(100)
	pw=p.apply_async(write,args=(q,))
	time.sleep(0.5)
	pr=p.apply_async(read,args=(q))
#	for s in dict1.keys():
#		print >> fout,"%s\t%s" % (s,dict1[s])
	p.close()
	p.join()
	print 'all over'
