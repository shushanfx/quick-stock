import cherrypy
import thread

import db
import index


class Stock(object):
  @cherrypy.expose
  @cherrypy.tools.json_out()
  def index(self, id, **kvargs):
    # return "HH"
    return db.fetch(id)

  @cherrypy.expose
  def run(self, id, **kvargs):
    thread.start_new_thread(index.get_it, (id, ))
    return 'done'

  @cherrypy.expose
  def runAll(self, **kvargs):
    thread.start_new_thread(index.get_all, tuple())
    return 'done'


if __name__ == '__main__':
  cherrypy.quickstart(Stock())