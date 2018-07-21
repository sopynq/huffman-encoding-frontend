# register address for huffman encoding core
# (SC = Self Clear, COR = Clear on Read, TOW = Toggle on Write, COH = Clear on Handshake)

# 0x0000 : Control signals
#          bit 0  - ap_start (Read/Write/COH)
#          bit 1  - ap_done (Read/COR)
#          bit 2  - ap_idle (Read)
#          bit 3  - ap_ready (Read)
#          bit 7  - auto_restart (Read/Write)
#          others - reserved
control_base_addr = 0x0000

# 0x0004 : Global Interrupt Enable Register
#          bit 0  - Global Interrupt Enable (Read/Write)
#          others - reserved
global_intr_en_addr = 0x0004

# 0x0008 : IP Interrupt Enable Register (Read/Write)
#          bit 0  - Channel 0 (ap_done)
#          bit 1  - Channel 1 (ap_ready)
#          others - reserved
ip_intr_en_addr = 0x0008

# 0x000c : IP Interrupt Status Register (Read/TOW)
#          bit 0  - Channel 0 (ap_done)
#          bit 1  - Channel 1 (ap_ready)
#          others - reserved
ip_intr_status_addr = 0x000c

# 0x1000 : Data signal of num_nonzero_symbols
#          bit 31~0 - num_nonzero_symbols[31:0] (Read)
sym_num_sig_addr = 0x1000

# 0x1004 : Control signal of num_nonzero_symbols
#          bit 0  - num_nonzero_symbols_ap_vld (Read/COR)
#          others - reserved
sym_num_cntr_addr = 0x1004

# 0x0400 ~
# 0x07ff : Memory 'symbol_histogram_value_V' (256 * 32b)
#          Word n : bit [31:0] - symbol_histogram_value_V[n]
sym_histo_val_base_addr = 0x0400

# 0x0800 ~
# 0x0bff : Memory 'symbol_histogram_frequency_V' (256 * 32b)
#          Word n : bit [31:0] - symbol_histogram_frequency_V[n]
sym_histo_freq_base_addr = 0x0800

# 0x0c00 ~
# 0x0fff : Memory 'encoding_V' (256 * 32b)
#          Word n : bit [31:0] - encoding_V[n]
encoding_base_addr = 0x0c00
