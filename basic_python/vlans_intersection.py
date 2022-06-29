command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
vlans1 = set(command1.split()[-1].split(','))
vlans2 = set(command2.split()[-1].split(','))
vlans = tuple(vlans1.intersection(vlans2))
print(sorted(vlans))