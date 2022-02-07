import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')
import requests
from bs4 import BeautifulSoup
import math

pref = 'wakayama'
pages = 1
url = 'https://www.minkou.jp/vcollege/search/pref='+pref+'/page=' + str(pages)
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select('.mod-pagerNum.mod-pagerNum__st')
count = math.floor(int(elems[1].span.text) / 10)
for i in range(count):
  url = 'https://www.minkou.jp/vcollege/search/pref='+pref+'/page=' + str(i+1)
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "html.parser")
  elems = soup.select('.schDetail-name-name')
  for elem in elems:
    print(elem.a.text)