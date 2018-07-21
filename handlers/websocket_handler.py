import tornado.websocket
from configs.default import *

from huffman_core_wrapper.preprocessor import *

class WebSocketHandler(tornado.websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True

  def open(self):
    pass

  # get text (only ascii supported)
  async def on_message(self, message):
    preprocessor = Preprocessor(message)
    freq_table = preprocessor.freq_table
    print(freq_table)

  def on_close(self):
    pass


