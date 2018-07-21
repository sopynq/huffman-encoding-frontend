import tornado.ioloop
import tornado.web
import tornado.websocket

from configs.default import *
from handlers.index_handler import IndexHandler
from handlers.websocket_handler import WebSocketHandler

from huffman_core_wrapper.huffman_encoding_core import *

def _main():
  # huffman encoding core instance
  huff_core_inst = HuffmanEncodingCore()

  router = [
    (r'/', IndexHandler),    
    (r'/ws', WebSocketHandler, dict(huff_core=huff_core_inst))
  ]

  app = tornado.web.Application(router)
  app.listen(conf_port)

  # run forever
  print('huffman encoding core coroutine server start!')
  tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
  _main()
  
