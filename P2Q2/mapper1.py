#!/usr/bin/env python3
import sys
import csv
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import random

dict_curry = {}
dict_harden = {}
dict_paul = {}
dict_james = {}

for line in sys.stdin:
  line = line.strip()
  line_list = line.split(',')

if len(line_list) > 21:
  player_col = line_list[21]
  shot_dist = line_list[12]
  defender_dist = line_list[18]
  shot_clock = line_list[9]
  shot_result = line_list[14]
  
  if len(shot_dist) != 0 and len(defender_dist) != 0 and len(shot_clock) != 0 and len(shot_result) != 0:
    shot_dist = float(shot_dist)
    defender_dist = float(defender_dist)
    shot_clock = float(shot_clock)
    
    if player_col == 'stephen curry':
      dict_curry[shot_dist, defender_dist, shot_clock] = ['stephen curry' , shot_result]
      c1 = random.sample(dict_curry.keys(),1)
   
    
    elif player_col == 'james harden':
      dict_harden[shot_dist, defender_dist, shot_clock] = ['james harden', shot_result]
      c2 = random.sample(dict_harden.keys(),1)
      
    elif player_col == 'chris paul':
      dict_paul[shot_dist, defender_dist, shot_clock] = ['chris paul',shot_result]
      c3= random.sample(dict_paul.keys(),1)
     
    elif player_col == 'lebron james':
      dict_james[shot_dist, defender_dist, shot_clock] = ['lebron james', shot_result]
      c4 = random.sample(dict_james.keys(),1)

      
    else:
      pass
  else:
    pass
else:
  pass

with open("myfile.txt", 'w') as f:

  f.write('%s\n' % (c1))
  f.write('%s\n' % (c2))
  f.write('%s\n' % (c3))
  f.write('%s\n' % (c4))
