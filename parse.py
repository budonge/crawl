#coding=utf8
import MySQLdb
import sys
import re
from multiprocessing import Pool,Process
reload(sys)
sys.setdefaultencoding("utf8")
fin=open("config","r")
def sp(a,b):
	fout=open("x"+str(a)+"-"+str(b),"w")
	print >> fout,"%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("网址","标书标题","加入日期","截止日期","招标编号","所属行业","地区","采招类型","招标机构","关键词")
	db=MySQLdb.connect(host='*******',user='******',passwd='******',db='******',charset='utf8')
	sql="SELECT url,content FROM crawl_enter WHERE us_id>='%d' and us_id<='%d'" % (a,b)
	cursor=db.cursor();
	cursor.execute(sql)
	results=cursor.fetchall()
	count=0
	for row in results:
		url=row[0]
		content=row[1]
		m1=re.search(r'\d{9}',url)
		if m1:
			flag="<url>"+m1.group()+"</url>"
		else:
			flag="<url>None</url>"
		m2=re.search(r'<h1 class="tc">(.*)',content)
		if m2:
			temp=re.sub(r'[\n\r\t]','',m2.group(1).strip())
			title="<title>"+temp+"</title>"
		else:
			title="<title>None</title>"
		m3=re.search(r'<td width="29%">(.*)</td>',content)
		if m3:
			temp=re.sub(r'[\n\r\t]','',m3.group(1).strip())
			start="<start>"+temp+"</start>"
		else:
			start="<start>None</start>"
		m4=re.search(r'<td width="32%">(.*)</td>',content)
		if m4:
			temp=re.sub(r'[\n\r\t]','',m4.group(1).strip())
			end="<end>"+temp+"</end>"
		else:
			end="<end>None</end>"
		m5=re.search(r'<th scope="row">招标编号：</th>[\r\n\t ]*<td>(.*)</td>[\r\n\t ]*<th>所属行业：</th>',content.encode('utf8'),re.S)
		if m5:
			temp=re.sub(r'[\r\n\t]','',m5.group(1).strip())
			if(0<len(temp)<100):
				number="<number>"+temp+"</number>"
			else:
				number="<number>None</number>"
		else:
			number="<number>None</number>"
		m6=re.search(r'<th>所属行业：</th>[\r\n\t ]*<td>(.*)</td>[\r\n\t ]*</tr>[\r\n\t ]*<tr>[\r\n\t ]*<th scope="row">地',content.encode('utf8'),re.M|re.S)
		if m6:
			temp=re.sub(r'[\r\n\t]','',m6.group(1).strip())
			if(0<len(temp)<100):
				industry="<industry>"+temp+"</industry>"
			else:
				industry="<industry>None</industry>"
		else:
			industry="<industry>None</industry>"
		m7=re.search(r'<th scope="row">地&nbsp;&nbsp;&nbsp;&nbsp;区：</th>[\r\n\t ]*<td>(.*)</td>[\r\n\t ]*<th>采招类型',content.encode('utf8'),re.M|re.S)
		if m7:
			temp=re.sub(r'[\r\n\t]','',m7.group(1).strip())
			if(0<len(temp)<50):
				area="<area>"+temp+"</area>"
			else:
				area="<area>None</area>"
		else:
			area="<area>None</area>"
		m8=re.search(r'<th>采招类型：</th>[\r\t\n ]*<td>(.*)</td>[\r\n\t ]*</tr>[\r\n\t ]*<tr>[\r\n\t ]*<th scope="row">招标机构',content.encode('utf8'),re.M|re.S)
		if m8:
			temp=re.sub(r'\n[\t ]{1,}','/',m8.group(1).strip())
			if(0<len(temp)<50):
				style="<style>"+temp+"</style>"
			else:
				style="<style>None</style>"
		else:
			style="<style>None</style>"
		m9=re.search(r'<th scope="row">招标机构：</th>[\r\n\t ]*<td colspan="3">(.*)<span class="spBtn">',content.encode('utf8'),re.M|re.S)
		if m9:
			temp=re.sub(r'[\r\n\t]','',m9.group(1).strip())
			if(0<len(temp)<100):
				organ="<organ>"+temp+"</organ>"
			else:
				organ="<organ>None</organ>"
		else:
			organ="<organ>None</organ>"
		m10=re.search(r'<th scope="row">关 键 词：</th>[\r\n\t ]*<td colspan="3">(.*)</td>[\r\n\t ]*</tr>[\r\n\t ]*</tbody></table>',content.encode('utf8'),re.M|re.S)	
		if m10:
			temp=re.sub(r'\n[\t ]{1,}','/',m10.group(1).strip())
		
			if(0<len(temp)<100):
				key="<key>"+temp+"</key>"
			else:
				key="<key>None</key>"
		else:
			key="<key>None</key>"
		print >> fout,"%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (flag,title,start,end,number,industry,area,style,organ,key)
		count+=1
		if(count%20000==0):
			print "%s\t%s" % ("x"+str(a)+"-"+str(b),count)
	db.close()
if __name__=='__main__':
	p=Pool(23)
	for line in fin:
		k=line.strip().split('\t')
		p.apply_async(sp,args=(int(k[0]),int(k[1])))
	p.close()
	p.join()
