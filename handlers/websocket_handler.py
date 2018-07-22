import tornado.websocket
from configs.default import *

from huffman_core_wrapper.preprocessor import *


class WebSocketHandler(tornado.websocket.WebSocketHandler):
  def initialize(self, huff_core):
    self.huff_core = huff_core

  def check_origin(self, origin):
    return True

  def open(self):
    pass

  # get text (only ascii supported)
  def on_message(self, message):
    preprocessor = Preprocessor(message)
    freq_table = preprocessor.freq_table
    encoding = self.huff_core.calc_encoding(freq_table)
    self.write_message(encoding)

  def on_close(self):
    pass


