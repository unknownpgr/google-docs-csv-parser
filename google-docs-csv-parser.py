import os
import csv
import re

for f in os.listdir('./'):
    if not f.endswith('.txt'):
        continue
    print(f)
    writer = csv.writer(open(f+'.csv', 'w', encoding='utf-8-sig', newline=''))
    row = ''
    annot = False
    for line in open(f, 'r', encoding='utf-8'):
        line = line.replace('* ', '').strip()
        if line.startswith('[') or annot:
            annot = True
            if line.startswith('['):
                if len(row) > 2:
                    writer.writerow([row.strip()])
                row = line
            else:
                row += line+'\n'
