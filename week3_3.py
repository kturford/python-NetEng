#!/usr/bin/env python
# week 3 exercise 3
# parse sho ip int bri output

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''
# split command output into list
split_int_bri = show_ip_int_brief.split()

# remove the headings from the list
split_int_bri = split_int_bri[6:]

# instantiate blank list to append later
interface = []

# go through 12 interface iterations
for i in range(0, 12):
    # pop the first element from the list
    int_name = split_int_bri.pop(0)
    ip_address = split_int_bri.pop(0)
    ok = split_int_bri.pop(0)
    method = split_int_bri.pop(0)
    status = split_int_bri.pop(0)
    protocol = split_int_bri.pop(0)

    #check for up/up status, set status to "reload" to break out of loop
    while status == "up" and protocol == "up":
        interface_tuple = (int_name, ip_address, status, protocol)
        interface.append(interface_tuple)
        status = "reload"

# screen output
print "{0:^15} {1:^15} {2:^15} {3:^15}".format("Int Name","IP Addr","Status", "Protocol")

for element in interface:
    # drop the tuple elements into variables
    (int_name,ip_addr,status,protocol) = element
    print "{0:^15} {1:^15} {2:^15} {3:^15}".format(int_name,ip_addr,status,protocol)
