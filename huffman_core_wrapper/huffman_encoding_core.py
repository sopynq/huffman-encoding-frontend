# Create only on instance of huffman encoding core
import os
from pynq import Overlay
import time
from huffman_core_wrapper.reg_table import *
import asyncio

class Singleton(object):
  def __new__(cls, *args, **kw):
    if not hasattr(cls, '_instance'):
      orig = super(Singleton, cls)
      cls._instance = orig.__new__(cls, *args, **kw)
    return cls._instance

# Actual Huffman encoding core wrapper
class HuffmanEncodingCore(Singleton):

  def __init__(self):
    self.overlay = Overlay('huffman_core_wrapper/bitstream/irq-test.bit')
    self.overlay.download()
    self.huff_core = self.overlay.huffman_encoding_0

  def start_calc(self):
    # enable interrupt
    self.huff_core.write(ip_intr_en_addr, 1)
    # read done interrupt
    self.huff_core.write(ip_intr_status_addr, 1)
    # start
    self.huff_core.write(ctrl_base_addr, 1)

  def feed_data(self, freq_table):
    if (not freq_table):
      return
    # write symbol and frequency to huffman core
    for idx, ele in enumerate(freq_table):
      # write to encoding core memory
      if (not ele == None):
        (val, freq) = ele
        self.huff_core.write(sym_histo_val_addr + 4*idx, ord(val))
        self.huff_core.write(sym_histo_freq_addr + 4*idx, freq)

  def read_code_word(self, freq_table):
    encoding = { 'symbol': [  ], 'total': 0 }
    for idx, ele in enumerate(freq_table):
      if (not ele == None):
        (val, freq) = ele
        encoding['symbol'].append(self.huff_core.read(encoding_addr + 4*ord(val)))
    encoding['total'] = self.huff_core.read(non_zero_cnt_data_addr)
    return encoding

  def calc_encoding(self, freq_table):
    self.feed_data(freq_table)
    start = time.time()
    self.start_calc()
    end = time.time()
    encoding = self.read_code_word(freq_table)
    return { 'encoding': encoding, 'consume': end - start }
    
    
