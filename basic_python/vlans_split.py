config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
commands = config.split()
vlans = commands[-1].split(',')
print(vlans)