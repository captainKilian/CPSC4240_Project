import urllib.request

suspiciousIPUrl = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"
filename = "suspicious_IP.txt"
urllib.request.urlretrieve(suspiciousIPUrl,filename)

f = open(filename, 'r')

print(f.read())