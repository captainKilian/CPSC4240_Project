import urllib.request

suspiciousIPUrl = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"
filename = "suspicious_IP.txt"
urllib.request.urlretrieve(suspiciousIPUrl,filename)

f_in = open(filename, 'r')
f_blocked = open("blocked_IPs.txt","r")

maliciousIPs = []

for line in f_in:
    if line[0] != '\n' and line[0] != '#':
        maliciousIPs.append(line.strip())

for line in f_blocked:
    if line[0] != '\n' and line[0] != '#':
        maliciousIPs.append(line.strip())

f_out = open(filename[:-4] + '_Prepared.txt','w')

for IP in maliciousIPs:
    f_out.write("\n" + IP)

f_out.close()
f_in.close()