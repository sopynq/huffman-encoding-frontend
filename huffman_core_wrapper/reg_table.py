# register address for huffman encoding core

# 0x0000 : Control signals
#          bit 0  - ap_start (Read/Write/COH)
#          bit 1  - ap_done (Read/COR)
#          bit 2  - ap_idle (Read)
#          bit 3  - ap_ready (Read)
#          bit 7  - auto_restart (Read/Write)
#          others - reserved
# 0x0004 : Global Interrupt Enable Register
#          bit 0  - Global Interrupt Enable (Read/Write)
#          others - reserved
# 0x0008 : IP Interrupt Enable Register (Read/Write)
#          bit 0  - Channel 0 (ap_done)
#          bit 1  - Channel 1 (ap_ready)
#          others - reserved
# 0x000c : IP Interrupt Status Register (Read/TOW)
#          bit 0  - Channel 0 (ap_done)
#          bit 1  - Channel 1 (ap_ready)
#          others - reserved
# 0x1000 : Data signal of num_nonzero_symbols
#          bit 31~0 - num_nonzero_symbols[31:0] (Read)
# 0x1004 : Control signal of num_nonzero_symbols
#          bit 0  - num_nonzero_symbols_ap_vld (Read/COR)
#          others - reserved
# 0x0400 ~
# 0x07ff : Memory 'symbol_histogram_value_V' (256 * 32b)
#          Word n : bit [31:0] - symbol_histogram_value_V[n]
# 0x0800 ~
# 0x0bff : Memory 'symbol_histogram_frequency_V' (256 * 32b)
#          Word n : bit [31:0] - symbol_histogram_frequency_V[n]
# 0x0c00 ~
# 0x0fff : Memory 'encoding_V' (256 * 32b)
#          Word n : bit [31:0] - encoding_V[n]
# (SC = Self Clear, COR = Clear on Read, TOW = Toggle on Write, COH = Clear on Handshake)


