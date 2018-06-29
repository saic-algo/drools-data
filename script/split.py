import json
import io
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
from datetime import timezone
import shutil

rawDir = '20121101'
splitDir = 'split'
splitTemplate = '{0}.csv'
if os.path.exists(splitDir):
    shutil.rmtree(splitDir)
os.makedirs(splitDir)

files = [f for f in listdir(rawDir) if isfile(join(rawDir, f))]
data = {}
for fname in files:
    raw = open(join(rawDir, fname), 'r')
    for line in raw:
        if(line == '\n'):
            continue

        id = line.split(',')[0]
        if(id not in data):
            data[id] = []
        data[id].append(line)

for id in data.keys():
    splitFile = open(splitTemplate.format(join(splitDir, id)), 'w')
    for line in data[id]:
        splitFile.write(line)
    splitFile.close()
