#coding=utf8
import urllib2,re
fout=open("sina","w")
url="http://weibo.com/u/3261172874/home?topnav=1&wvr=6"
headers={'User-Agent':'','Cookie':'UOR=os.51cto.com,widget.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW9QGIi0ilkAW7aRaY1oL_K5JpX5K2t; SINAGLOBAL=9308577578734.305.1437033026393; ULV=1439522461349:16:4:4:5641775812477.34.1439522461338:1439445095954; SUHB=04WektxQk1vI8Y; myuid=3261172874; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; SUB=_2A254yRXBDeTxGeVM7VMQ9yzEzDiIHXVbvwAJrDV8PUNbuNAPLWPfkW93VfU1BeM1R3L_DeF8X3ZD3Lu7KA..; _s_tentry=login.sina.com.cn; Apache=5641775812477.34.1439522461338; login_sid_t=5ae14dbd3acc08d88ab5db07a5b05718; un=budongyufan@sina.cn; TC-V5-G0=40eeee30be4a1418bde327baf365fcc0; SUS=SID-3261172874-1439524241-XD-d1k4a-779f24e54c9ce1d96d6d1f4f40ecf8dd; SUE=es%3Dbd3d408748ec7712174766376575dc67%26ev%3Dv1%26es2%3D38e5c9ad4a12a62846fe5567fa01d487%26rs0%3DZjldAVNHCk6V7GRGzhP8DjJJJJm8v1yLt67aZxDGl5%252FYxvWuuYq%252FJQ4wPCrJ8EqnBCUWgFfyeKjWCX8KL%252FNexeY4zCPdCG5QNGNv1ZleY3S4fzzY95eQk4fVqDaYxqnPqbafXS07uKAtR3s5lhgqeyR%252FOPQhFxuqDwjt2dnNvxY%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1439524241%26et%3D1439610641%26d%3Dc909%26i%3Df8dd%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D3261172874%26name%3Dbudongyufan%2540sina.cn%26nick%3Dbudong%26fmp%3D%26lcp%3D; ALF=1471060241; SSOLoginState=1439524241'}
req=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(req)
page=response.read()
hehe=re.sub(r'[\w\\/<>=".-?:\[\]\$ ]','',page)
print >> fout,hehe
