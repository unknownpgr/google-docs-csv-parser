import os
import csv
import re

for d in os.listdir('./'):
    if os.path.isfile(d):
        continue
    if d.startswith('.'):
        continue
    writer = csv.writer(open(d+'.csv', 'w', encoding='utf-8-sig', newline=''))
    for f in os.listdir(d):
        if not f.endswith('.txt'):
            continue
        p = re.search('P[0-9]+', f).group(0)
        print(d, p)
        row = ''
        annot = False
        for line in open(d+'/'+f, 'r', encoding='utf-8'):
            line = line.replace('* ', '').strip()
            if line.startswith('[') or annot:
                annot = True
                if line.startswith('['):
                    if len(row) > 2:
                        writer.writerow(
                            [p, d, row.strip()])
                    row = line
                else:
                    row += line+'\n'
