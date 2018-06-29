import json
import io
import os
import sys
import csv
from os import listdir
from os.path import isfile, join
from datetime import datetime
from datetime import timezone
from random import randint
import shutil
import operator

rawDir = 'raw'
sortDir = 'sort'
if os.path.exists(sortDir):
    shutil.rmtree(sortDir)
os.makedirs(sortDir)

files = [f for f in listdir(rawDir) if isfile(join(rawDir, f))]
for fname in files:
    reader = csv.reader(open(join(rawDir, fname), 'r'))
    sortedlist = sorted(reader, key=operator.itemgetter(3))
    resultFile = open(join(sortDir, fname), 'w')
    preLine = []
    for line in sortedlist:
        if(len(preLine) > 3 and line[3] == preLine[3]):
            continue
        preLine = line
        resultFile.write(','.join(line))
        resultFile.write('\n')
