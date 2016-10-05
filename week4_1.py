#!/usr/bin/env python
# week 4 exercise 1
# check ip validity, prompt user if IP not valid

# instantiate ip_valid to true
ip_valid = 0

# begin while loop
while True:

    # prompt user for IP Address
    ip_addr = raw_input("Please Enter IP Address:  ")
    ip_addr = ip_addr.split(".")

    while ip_valid == 0:
        #Check that the IP address contains 4 octets.
        if len(ip_addr) == 4:
            ip_valid = 1
        else:
            ip_valid = 0
            break

        #The first octet must be between 1 - 223.
        if int(ip_addr[0]) <= 223 and int(ip_addr[0]) >= 1:
            ip_valid = 1
        else:
            ip_valid = 0
            break

        #The first octet cannot be 127.
        if int(ip_addr[0]) != 127:
            ip_valid = 1
        else:
            ip_valid = 0
            break

        #The IP address cannot be in the 169.254.X.X address space.
        if int(ip_addr[0]) != 169 and int(ip_addr[1]) != 254:
            ip_valid = 1
        else:
            ip_valid = 0
            break

        #The last three octets must range between 0 - 255.
        for element in ip_addr:
            if int(element) <= 255 and int(element) >=0:
                ip_valid = 1
            else:
                ip_valid = 0
                break

    if ip_valid == 0:
        print "IP Address %s is not valid" % ".".join(ip_addr)
    else:
        break

# check for ip_valid status and output pass/fail
print "IP Address %s is valid" % ".".join(ip_addr)
