import urllib.request

suspiciousIPUrl = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"
filename = "suspicious_IP.txt"
urllib.request.urlretrieve(suspiciousIPUrl,filename)

f_in = open(filename, 'r')

# print(f.read())

maliciousIPs = []

for line in f_in:
    if line[0] != '\n' and line[0] != '#':
        maliciousIPs.append(line.strip())
        # print(line)

# print(filename[:-4] + '_Prepared.txt')
f_out = open(filename[:-4] + '_Prepared.txt','w')

for IP in maliciousIPs:
    f_out.write(IP + "\n")

f_out.close()
f_in.close()