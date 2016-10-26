#     __ __ _   ______  ________ __      __ __ _   ______  ________ __
#    / //_// | / / __ \/ ____/ //_/     / //_// | / / __ \/ ____/ //_/
#   / ,<  /  |/ / / / / /   / ,<       / ,<  /  |/ / / / / /   / ,<
#  / /| |/ /|  / /_/ / /___/ /| |     / /| |/ /|  / /_/ / /___/ /| |
# /_/ |_/_/ |_/\____/\____/_/ |_|    /_/ |_/_/ |_/\____/\____/_/ |_|  PORT SCANNER V1.0

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Author: Umar Javed
# Date: 26/10/2016
# Version: 1.0
# Notes: requires Python v2 I.e. 2.7.12
# DISCLAIMER: This tool is intended for educational and research purposes so feel free to chop, change, rip apart, fork
# or do whatever you like with the code but if you use it on production systems, do so only with the express permission
# of the owner of the networks that you intend to scan.  Play nice, play fair, don't be evil!
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

from socket import *
import time

# Used to timestamp the start of the scan
localtime = time.asctime(time.localtime(time.time()))

# This variable can be tailored to your needs, add or remove ports to include in the scan.
common_ports = [20,  # FTP (File Transfer Protocol)
                21,  # FTP (File Transfer Protocol)
                22,  # SSH (Secure Shell)
                23,  # Telnet
                25,  # SMTP (Simple Mail Transfer Protocol)
                53,  # DNS (Domain Name System)
                67,  # DHCP (Dynamic Host Control Protocol)
                68,  # DHCP (Dynamic Host Control Protocol)
                69,  # TFTP (Trivial File Transfer Protocol)
                80,  # HTTP
                110,  # POP3 (Post Office Protocol v3)
                123,  # NTP (Network Time Protocol)
                137,  # NetBIOS
                138,  # NetBIOS
                139,  # NetBIOS
                143,  # IMAP (Internet Message Access Protocol)
                161,  # SNMP (Simple Network Management Protocol)
                162,  # SNMP (Simple Network Management Protocol)
                179,  # BGP (Border Gateway Protocol)
                389,  # LDAP
                443,  # HTTP over TLS/SSL (HTTPS)
                636]  # LDAP over TLS/SSL (LDAPS)

# Empty lists we'll use to store the ports that are open/closed whilst the scan is running
open_ports = []
closed_ports = []

# Accept user input of an IP address or hostname
scantarget_input = raw_input("Enter hostname or the IP address to scan: ")
scantargetIP = gethostbyname(scantarget_input)

# This is where the magic happens
if __name__ == '__main__':
    print "Starting scan on host" + " " + str(scantargetIP) + " " + "on" + " " + str(localtime)

# For loop reads the common_ports variable against each hostname/ip and checks to see if the ports are Open or Closed
# and then appends the results to the appropriate empty list variables: open_ports and closed_ports
for i in common_ports:
        s = socket(AF_INET, SOCK_STREAM)  # Socket family can be change from IPv4 AF_INET to IPV6 AF_INET6
        result = s.connect_ex((scantargetIP, i))
        if result == 0:
            print "Port %d: ........ OPEN " % (i,)
            open_ports.append(i)
        else:
            print "Port %s: closed" % (i,)
            closed_ports.append(i)
        s.close() # Terminates the socket connection

# variable used to convert the variable value for open_ports from an integer to a string
open_port_count = len(open_ports) # converts integer to string
print "\n====SUMMARY====:"
print "Scan completed, there are"+" "+str(open_port_count)+" "+"OPEN ports and these are:"+" "+str(open_ports)
