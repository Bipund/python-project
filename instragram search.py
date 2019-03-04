import re
import urllib.request
#https://www.google.com/search?tbm=fin&ei=H_qsWvfKOpiavQSbjKy4Cw&q=goog
url="https://www.instagram.com/"
stock = input("enter instagram user id")
url=url+stock
data = urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

m=re.search('meta content="',data1)
start=m.start()
end=start+51

nn=data1[start:end]

m=re.search('meta content="',nn)
start=m.start()+14
end=start+40
fin=nn[start:end]
print("the instagram detail is shown below for\n",stock)
print("is shown\n",fin)






