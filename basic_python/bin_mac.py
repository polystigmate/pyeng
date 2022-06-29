mac = 'AAAA:BBBB:CCCC'
bin_mac = '{:b}'.format(int(mac.replace(':', ''), 16))
print(bin_mac)