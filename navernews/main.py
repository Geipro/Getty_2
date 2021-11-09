from fastapi import FastAPI
from pydantic import BaseModel
import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
from typing import Optional



app = FastAPI()

class News(BaseModel):
    title: str
    url: str
    thumbnail: str

@app.get("/")
async def root():
	return { "message" : "Hello World" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/news/{query}")
def read_item(query: str):
    print(query)
    query = query.replace(' ', '+') 
    # news_num = int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : '))
    news_num = 10
    news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'
    req = requests.get(news_url.format(query))
    soup = BeautifulSoup(req.text, 'html.parser')

    news_dict = {} 
    idx = 0 
    # cur_page = 1

    table = soup.find('ul',{'class' : 'list_news'})
    li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
    area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
    a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
    thumbnail_list = [li.find('a', {'class': 'dsc_thumb'}).find('img') for li in li_list]

    for n in a_list[:min(len(a_list), news_num-idx)]:
        news_dict[idx] = {'title' : n.get('title'),
                          'url' : n.get('href'),
                          }
        idx += 1

    idx = 0

    for n in thumbnail_list[:min(len(thumbnail_list), news_num-idx)]:
        news_dict[idx]['thumbnail'] = n.get('src'),
        idx += 1

    return news_dict
    # return {"query": query}


# @app.post('/news/')
# async def crawl_news(news: News):
#   query = query.replace(' ', '+') 
#   # news_num = int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : '))
#   news_num = 10
#   news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'
#   req = requests.get(news_url.format(query))
#   soup = BeautifulSoup(req.text, 'html.parser')

#   news_dict = {} 
#   idx = 0 
#   # cur_page = 1

#   table = soup.find('ul',{'class' : 'list_news'})
#   li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
#   area_list = [li.find('div', {'class' : 'news_area'}) for li in li_list]
#   a_list = [area.find('a', {'class' : 'news_tit'}) for area in area_list]
#   thumbnail_list = [li.find('a', {'class': 'dsc_thumb'}).find('img') for li in li_list]

#   for n in a_list[:min(len(a_list), news_num-idx)]:
#       news_dict[idx] = {'title' : n.get('title'),
#                         'url' : n.get('href'),
#                         }
#       idx += 1

#   idx = 0

#   for n in thumbnail_list[:min(len(thumbnail_list), news_num-idx)]:
#       news_dict[idx]['thumbnail'] = n.get('src'),
#       idx += 1

# 	return news_dict