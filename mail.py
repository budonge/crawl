#encoding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import datetime
import time
import os


TODAY = datetime.date.today()
CURRENTDAY=TODAY.strftime('%Y%m%d')
def sendattachmail ():
	msg = MIMEMultipart()
	att=MIMEText(open(r'/mnt/yufan/log.txt','rb').read(),'base64','utf-8')
	att['content-type']='application/octet-stream'
	att['content-disposition']='attachment;filename="log.txt"'
	msg.attach(att)
	
	content = '附件请查收'  #正文内容
	body = MIMEText(content,'plain','utf-8') #设置字符编码
	msg.attach(body)
	msgto = ['weifang.wen@salespro.cn','fan.yu@salespro.cn']
	msgfrom = 'fan.yu@salespro.cn' # 寄信人地址
	msg['subject'] = CURRENTDAY+'  必联今日抓取情况'  #主题
	msg['date']=time.ctime() 
	msg['Cc']='data@salespro.cn'
	mailuser = 'fan.yu@salespro.cn'  # 用户名
	mailpwd = 'Beyond123' #密码
	try:
		smtp = smtplib.SMTP()
		smtp.connect(r'smtp.mxhichina.com')# smtp设置
		smtp.login(mailuser, mailpwd) #登录
		smtp.sendmail(msgfrom, msgto, msg.as_string()) #发送
		smtp.close()
	except Exception, e:
		print e
   

if __name__ == '__main__':
	sendattachmail()
