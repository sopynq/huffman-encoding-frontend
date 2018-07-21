# Create only on instance of huffman encoding core
import os
from pynq import Overlay
from huffman_core_wrapper.reg_table import *

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
    print(freq_table)
    
    # write symbol and frequency to huffman core
    for idx, ele in enumerate(freq_table):
      # write to encoding core memory
      if (not ele == None):
        (val, freq) = ele
        self.huff_core.write(sym_histo_val_addr + 4*idx, ord(val))
        self.huff_core.write(sym_histo_freq_addr + 4*idx, freq)

  async def calc_encoding(self, freq_table):
    feed_data(freq_table)
    start_calc()
        # wait until done
    from time import sleep
    sleep(1)
    
    # read them out
    print(self.huff_core.read(non_zero_cnt_data_addr))
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    for ele in freq_table:
      if (not ele == None):
        offset = ord(ele[0])
        print(get_bin(self.huff_core.read(encoding_addr + 4*offset), 32))


#   async def huff_intr_handler(huff):
#     while True:
#       await huff.interrupt.wait()
#       print('intr received from ' + str(huff.read(0x000c)))
#       if (huff.read(0x000c) == 1):
#         # read number of symbols
#         num = huff.read(0x1000)
#         print('There are ' + str(num) + ' symbols in huffman tree:')
#
#         # read encoding
#         get_bin = lambda x, n: format(x, 'b').zfill(n)
#         for idx, sym in enumerate(symbol_table):
#           encoding = huff.read(0x0c00 + 4*ord(sym['symbol']))
#           print('symbol : ' + sym['symbol'] + ', code word : ' + get_bin(encoding, 32))
#       if (huff.read(0x000c) & 0x1):
#         huff.write(0x000c, 1)
#
#   # get EventLoop:
#   loop = asyncio.get_event_loop()
#   # run coroutine
#   loop.run_until_complete(huff_intr_handler(huffman_encoding))
#   loop.close()
