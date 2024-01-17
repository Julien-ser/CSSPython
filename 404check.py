'''log_file = "log20230630.csv"
f = open(log_file, "r")
while True:
    line = f.readline()
    if not line:
        break
    if "404" in line:
        print(line.strip())

f.close()'''

import re

log_file = "log20230630.csv"
f = open(log_file, "r", encoding="utf8")
sample_logs = f.readlines()
client_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
clientdict = {}

for line in sample_logs:
    m = re.search(client_pattern, line)
    if m:
        client = m.group()
        if client in clientdict.keys():
            clientdict[client] += 1
        else:
            clientdict[client] = 1

for w in sorted(clientdict, key=clientdict.get, reverse=False):
    print(w, clientdict[w])
    
