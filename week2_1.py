# week2 python exercise 1

# prompt user for Network Subnet
net_addr = raw_input("Please Enter IP Address:  ")

# set last octet to '0'
net_addr = net_addr.split('.')

# extract first octet
first_oct = int(net_addr[0])

# replace last octet
net_addr[3] = '0'

# rejoin to make IP Address
net_addr = ".".join(net_addr)


# print the subnet
print "The network number is: %s" % first_oct
print "{0:^15} {1:^15} {2:^15}".format("Network","Hex","Binary")
print "{0:^15} {1:^15} {2:^15}".format(net_addr,hex(first_oct),bin(first_oct))
