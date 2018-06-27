#!/usr/bin/env python

from config import Config
import db

from time import sleep
import requests
import math
import random
import demjson
import re
import codecs
# import js2py

def fetch_total(stock_id):
  url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssc_qsfx_lscjfb'
  data = {}
  data['daima'] = stock_id
  r = requests.get(url, params=data)
  text = r.text
  match = re.search('(\\d+)', text)
  if match:
    a_str = match.group(1)
    return int(a_str)
  return 0

def fetch_list(stock_id, page_index = 1, page_size = 200):
  url = ' http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_qsfx_lscjfb?page=1&num=200&sort=opendate&asc=0&daima=sh600606'
  data = {}
  data['daima'] = stock_id
  data['page'] = page_index
  data['num'] = page_size
  data['sort'] = 'opendate'
  data['asc'] = 0
  r = requests.get(url, params=data)
  # text = "new function(){return %s;}" % (r.text)
  # obj = js2py.eval_js(text)
  print 'Get stock %s of page %d' % (stock_id, page_index)
  obj = demjson.decode(r.text)

  return obj

def index_of(a_item, target_list):
  for index, item in enumerate(target_list):
    if item.get('opendate') == a_item.get('opendate'):
      return index
  return -1

def sleep_it(step = 5):
  i_time = math.ceil(random.random() * step)
  print 'Sleep for %d' % (i_time, ) 

def save_to(new_list, target_list):
  for item in new_list:
    index = index_of(item, target_list)
    #print index
    if index != -1:
      target_list[index] = item
    else:
      target_list.append(item)

def get_it(stock_id):
  print 'Fetch stock ', stock_id
  total = fetch_total(stock_id)
  a_list = list()
  i_index = 1
  i_size = 200
  i_total = math.ceil(total / i_size)
  while i_index  <= i_total :
    new_list = fetch_list(stock_id, i_index, i_size)
    save_to(new_list, a_list)
    i_index = i_index + 1
  db.save(stock_id, a_list)
  print 'Save %s successfully.' % (stock_id, ) 

def get_all():
  conf = Config('./config.conf')
  a_list = conf['stock']
  for item in a_list:
    print 'Fetch stock ', item[1], item[0]
    sleep_it(100)
    get_it(item[0])

if __name__ == '__main__':
  get_all()