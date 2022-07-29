#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys

for line in sys.stdin:
        line = line.strip()
        line_list = line.split(',')
        
        if len(line_list)> 32:           
            if len(line_list[33])!= 0 and line_list[33].isalpha():                
                print('%s\t%s' % (line_list[33], 1))                
        else:
            pass
