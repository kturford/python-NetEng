#!/usr/bin/env python
# week4 exercise 2
# parse Cisco Show version
# Store these variables (vendor, model, os_version, uptime, and serial_number) in a dictionary.
# Print the dictionary to standard output when done.

show_version_output = """Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102"""

parse_shversion = show_version_output.split('\n')

first_line = parse_shversion[0].split(',')

# vendor name
vendor = first_line[0].split(' ')
vendor = vendor[0]

#os_version
os_ver = first_line[2].split(' ')
os_ver = os_ver[2]

#model
model = parse_shversion[13].split(' ')
model = " ".join(model[:6])

# uptime
uptime = parse_shversion[6].split(' ')
uptime = " ".join(uptime[3:])

# serial_number
sn = parse_shversion[26].split(' ')
sn = sn[-1]

# build the dictionary
host = {}
host['vendor'] = vendor
host['os_version'] = os_ver
host['model'] = model
host['uptime'] = uptime
host['serial_number'] = sn

# output the Information

print "Vendor is: " + host['vendor']
print "OS Version: " + host['os_version']
print "Model: " + host['model']
print "System Uptime: " + host['uptime']
print "Serial Number: " + host['serial_number']
