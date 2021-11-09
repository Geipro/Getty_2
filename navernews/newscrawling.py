import requests
from bs4 import BeautifulSoup
import re

# query = input('검색 키워드를 입력하세요 : ') 

def news_crawling(query):
  query = query.replace(' ', '+') 

  news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'

  req = requests.get(news_url.format(query))
  soup = BeautifulSoup(req.text, 'html.parser')

  news_dict = {} 

  table = soup.find('ul',{'class' : 'list_news'})
  li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
  area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
  a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
  thumbnail_list = [li.find('a', {'class': 'dsc_thumb'}).find('img') for li in li_list]

  for i in range(10):
    n = a_list[i]
    news_dict[i] = {
      'title' : n.get('title'),
      'url' : n.get('href'),
      }
    news_dict[i]['thumbnail'] = thumbnail_list[i].get('src')

  return news_dict

if __name__ == "__main__":
  query = '코로나'
  # query = input('검색 키워드를 입력하세요 : ') 
  news_crawling(query)