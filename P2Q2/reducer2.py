#!/usr/bin/env python3
import sys
import csv
import re

newfile= open("newfile.txt","a+")

with open ("myfile.txt", "r+") as f:

  for line in f:
    
    line = re.sub(r"[\[\]]","",line)
    line = line.replace('(','').replace(')','')
    newfile.write(line)
    print(line)
