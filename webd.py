import cherrypy
from cherrypy.process.plugins import Daemonizer

import web

if __name__ == '__main__':
  d = Daemonizer(cherrypy.engine)
  d.subscribe()
  cherrypy.quickstart(web.Stock())