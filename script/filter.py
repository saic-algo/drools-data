import json
import io
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
from datetime import timezone
from random import randint
import shutil

rawDir = 'split'
filterDir = 'filter'
filterTemplate = '{0}_{1}.csv'
if os.path.exists(filterDir):
    shutil.rmtree(filterDir)
os.makedirs(filterDir)

files = [f for f in listdir(rawDir) if isfile(join(rawDir, f))]
for fname in files:
    raw = open(join(rawDir, fname), 'r')
    content = raw.readlines()

    start = -1
    count = 0
    for i in range(len(content)):
        if(content[i].split(',')[1] == '1'):
            start = i
            continue

        if(content[i].split(',')[1] == '0' and start >= 0):
            if(i - start < 10):
                start = -1
                continue
            id = content[i].split(',')[0]
            begin = start - 1
            for _ in range(randint(3,9)):
                condition = content[begin - 1].split(',')[1]
                if(condition == '0'):
                    begin -= 1
                    break
                elif(condition == '2' or condition == '3'):
                    break
                else:
                    begin -= 1

            resultFile = open(filterTemplate.format(join(filterDir, id), count), 'w')
            for j in range(begin, i+1):
                resultFile.write(content[j])
            count += 1
            start = -1