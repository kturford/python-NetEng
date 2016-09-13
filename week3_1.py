#!/usr/bin/env python
# week 3 exercise 1
# create a binary_converter

# use the 1st argument for the conversion
import sys
ip_addr = sys.argv[1]

#split address into octets
split_ip_addr = ip_addr.split('.')

# create octet_bin blank list
octet_bin = []

# convert decimal octets to binary, strip 0b
for i,j in enumerate(split_ip_addr):
    octet = (int(j))
    octet = bin(octet)
    octet = octet.split('b')
    octet = octet[1]

# prepend with zeroes to 8 characters
    while len(str(octet)) < 8:
        octet = '0' + octet

    octet_bin.append(octet)

# join binary octets to dotted notation
ip_addr_bin = ".".join(octet_bin)

# formatted output
print "{0:^15} {1:^15}".format("IP Address","Binary")
print "{0:^15} {1:^15}".format(ip_addr,ip_addr_bin)
