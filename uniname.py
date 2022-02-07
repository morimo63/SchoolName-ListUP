import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')
import requests
from bs4 import BeautifulSoup

preNum = 25
url = 'https://passnavi.evidus.com/search_univ/list/pre_' +str(preNum) +'/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select('li a')

judge = False
count = 0
for elem in elems:
    if '北海道' in elem.text:
      judge = False1
    if judge:
      print(elem.text)
    if '大学受験パスナビTOP' in elem.text:
      count += 1
      if count == 2:
        judge = True
