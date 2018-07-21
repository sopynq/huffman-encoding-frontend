import tornado.ioloop
import tornado.web
import tornado.websocket

from configs.default import *
from handlers.index_handler import IndexHandler
from handlers.websocket_handler import WebSocketHandler

router = [
  (r'/', IndexHandler),    
  (r'/ws', WebSocketHandler)
]

if __name__ == '__main__':
  app = tornado.web.Application(router)
  app.listen(conf_port)
  tornado.ioloop.IOLoop.current().start()
