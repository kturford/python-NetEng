#!/usr/bin/env python
# week 4 exercise 3
"""
Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name as the key.

During this conversion process, you will have to convert strings to integers.  For these string to integer conversions use try/except to catch any string to integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.
"""

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

# dictionary instantiation
routers = {}

# set total_secs to 0 and split the uptime output for each uptime
for hosts in (uptime1, uptime2, uptime3, uptime4):
    total_secs = 0
    hosts = hosts.split()

    for element in hosts:
        # pull weeks and multiply by 604800 (seconds in a week)
        if 'weeks,' in element:
            weekvalue = hosts.index(element) - 1
            weekvalue = int(hosts[weekvalue]) * 604800
        else:
            weekvalue = 0

        # pull days and multiply by 86400
        if 'days,' in element:
            dayvalue = hosts.index(element) - 1
            dayvalue = int(hosts[dayvalue]) * 86400
        else:
            dayvalue = 0

        # pull minutes and multiply by 60
        if 'minutes' in element:
            minvalue = hosts.index(element) - 1
            minvalue = int(hosts[minvalue]) * 60
        else:
            minvalue = 0

        total_secs = total_secs + int(weekvalue) + int(dayvalue) + int(minvalue)

    print total_secs

    # put together and enter into routers dictionary
    routers[hosts[0]] = total_secs

print routers
