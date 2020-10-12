import os
import csv
for f in os.listdir('./'):
  if not f.endswith('.txt'):
    continue
  writer=  csv.writer()
  txt = open(f,'r',encoding='utf-8').read()
  txt.split('\n\n')
  print(txt[-1])