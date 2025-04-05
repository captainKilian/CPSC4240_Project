import sys
import re

f = open("blocked_IPs.txt",'a')

valid_IP_Pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}(\/\d{1,2})?$')

for IP in sys.argv[1:]:
    if valid_IP_Pattern.match(IP):
        ip = IP.split('/')
        numbers = ip[0].split('.')
        for number in numbers:
            if int(number) > 255 or int(number) < 0 and number.isdigit():
                print("Invalid IP:",IP)
                quit()
        if len(ip) == 2 and (int(ip[1]) > 32 or int(ip[1]) < 0) and ip[1].isdigit():
            print("Invalid IP:",IP)
            quit()
        print('Writing IP:', IP)
        f.write('\n' + IP)
    else:
        print("Invalid IP:",IP)
        quit()
