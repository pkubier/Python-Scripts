url='https://www.linkedin.com/search/results/people/?network=%5B%22F%22%2C%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&schoolFilter=%5B%2219177%22%5D'
import bs4
import requests
res=requests.get(url)
soup=bs4.BeautifulSoup(res.text, 'lxml')
