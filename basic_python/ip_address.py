ip = '192.168.3.1'
oct1, oct2, oct3, oct4 = ip.split('.')
ip_template = '''
    IP address:
    {0:<8} {1:<8} {2:<8} {3:<8} 
    {0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(oct1), int(oct2), int(oct3), int(oct4)))