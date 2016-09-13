# week2 python exercise 2
# create an IP address converter (dotted decimal to binary)

# prompt user for Network Subnet
net_addr = raw_input("Please Enter IP Address: ")

# split net_addr to list
net_addr = net_addr.split('.')

# variables for list elements - as int
first_oct = int(net_addr[0])
sec_oct = int(net_addr[1])
third_oct = int(net_addr[2])
fourth_oct = int(net_addr[3])

print "{0:^15} {1:^15} {2:^15} {3:^15}".format("First Octet","Second Octet","Third Octet","Fourth Octet")
print "{0:^15} {1:^15} {2:^15} {3:^15}".format(bin(first_oct),bin(sec_oct),bin(third_oct),bin(fourth_oct))
