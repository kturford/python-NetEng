# week 2 exercise 4
# distill ios_version from cisco_ios

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

cisco_ios = cisco_ios.split(",")
print cisco_ios

print "\n"

version_str = cisco_ios[2]
version_str = version_str.split()

ios_version = version_str[1]

print "Cisco IOS version: " + ios_version
