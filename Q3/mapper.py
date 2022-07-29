#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    line_list = line.split(',')

    if len(line_list)>=25:
        #strip white space from each cell value 
        line_list[23] = line_list[23].strip()
        line_list[24] = line_list[24].strip()            
        
        if len(line_list[24])!=0:
            print('%s,%s\t%s' % (line_list[23], line_list[24], 1))
            #print('%s\t%s' % (line_list[24], 1))

        else:
            pass
    else:
        pass
