import requests
import lxml
from bs4 import BeautifulSoup
res = requests.get('https://codedamn.com')

print(res.text)
print(res.status_code)