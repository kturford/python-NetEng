# week2 python exercise 3
# parse show ip bgp output

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

print "{0:^10} {1:^15}".format("ip_prefix","as_path")

for i in range(4):
    current_entry = ("entry" + (str(i+1)) % locals())
    print current_entry
    #print "{0:^10} {1:^15}".format(current_entry[2],current_entry[4:-1])
    print entry1
