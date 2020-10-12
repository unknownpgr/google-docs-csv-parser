import os
import csv

for f in os.listdir('./'):
    if not f.endswith('.txt'):
        continue
    writer = csv.writer(open(f+'.csv', 'w', encoding='utf-8-sig', newline=''))
    for line in open(f, 'r', encoding='utf-8'):
        if line.startswith('['):
            writer.writerow([line.replace("\r","").replace('\n','')])
