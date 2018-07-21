from collections import Counter

class Preprocessor():
  # frequency table
  freq_table = [ ]
  encoding_str = ''

  def __init__(self, encoding_str):
    # calculate freq table
    self.encoding_str = encoding_str
    self.freq_table = self.calculate_freq()

  def calculate_freq(self):
    return Counter(self.encoding_str).items()
