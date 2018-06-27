import ConfigParser
import codecs

class Config(object):
  __cf = None

  def __init__(self, file_path):
    conf = ConfigParser.ConfigParser()
    a_file = codecs.open(file_path, 'r', encoding='utf-8')
    conf.readfp(a_file, file_path)
    self.__cf = conf

  def __getitem__(self, key):
    keys = key.split('.')
    try:
      if len(keys) >= 2:
        return self.__cf.get(keys[0], keys[1])
      elif len(keys) == 1:
        return self.__cf.items(keys[0])
    except:
      pass
    return None

if __name__ == '__main__':
  c = Config('./config.conf')
  print c['db.port']
  print c['db.xx']
  print c['db']