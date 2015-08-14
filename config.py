#coding=utf8
fout=open("config","w")
min1=5911428
max1=8175025
p=23
deta=(max1-min1)/p
print >> fout,"%s\t%s" % (str(min1),str(min1+deta))
min1=min1+deta+1
for i in range(p-2):
	print >> fout,"%s\t%s" % (str(min1),str(min1+deta))
	min1=min1+deta+1

print >> fout,"%s\t%s" % (str(min1),str(max1))
