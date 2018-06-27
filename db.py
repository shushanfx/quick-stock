import os.path
import codecs
import demjson

def save(stock_id, a_list):
  file_path = os.path.join('./data', stock_id + '.json')
  return demjson.encode_to_file(file_path, a_list, encoding ='utf-8', overwrite=True, compactly = False)

def fetch(stock_id):
  file_path = os.path.join('./data', stock_id + '.json')
  return demjson.decode_file(file_path, encoding='utf-8')



