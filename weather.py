import re
import urllib.request
#https://www.weather-forecast.com/locations/New-York/forecasts/latest
city=input("enter city ot check weather")
url="https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

m=re.search('class="phrase"',data1)
start=m.start()+15
end=start+80
nn=data1[start:end]
print(nn)

