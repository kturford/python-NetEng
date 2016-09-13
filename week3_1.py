#!/usr/bin/env python
# week 3 exercise 1
# create a binary_converter

# use the 1st argument for the conversion
import sys
ip_addr = sys.argv[1]

#split address into octets
ip_addr = ip_addr.split('.')

print ip_addr

for i,j in enumerate(ip_addr):
    #octet+str(i) = ip_addr[j]
    print i
    print j
#print octet0
#print octet1
#print octet2
#print octet3
    ip_addr_bin.append(bin(int(j)))
    print ip_addr_bin
