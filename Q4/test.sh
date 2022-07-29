#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1Q4_v2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1Q4_v2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Part1Q4_v2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-python/project1/Parking_Violations_Issued_-_Fiscal_Year_2021.csv /Part1Q4_v2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/Part1Q4_v2/mapper_p1q4.py -mapper ../../mapreduce-test-python/Part1Q4_v2/mapper_p1q4.py \
-file ../../mapreduce-test-python/Part1Q4_v2/reducer_p1q4.py -reducer ../../mapreduce-test-python/Part1Q4_v2/reducer_p1q4.py \
-input /Part1Q4_v2/input/* -output /Part1Q4_v2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /Part1Q4_v2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1Q4_v2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Part1Q4_v2/output/
../../stop.sh
