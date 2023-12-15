# IST3134-19046739
This is part of a submission for a subject (IST3134 - Big Data Analytics in the Cloud). The assignment required us to design a task that involves processing big data and compare different methods of achieving it. 
Methods compared in this assignment included:
- Conventional approach (Python)
- MapReduce on local machine
- MapReduce on Hadoop cluster
- Apache Hive on Hadoop cluster

Explanation of directory for relevant files

hadoop_cluster/hive_output: Contain partial outputs from Apache Hive (Before concatenation)  
hadoop_cluster/output: Contain output of MapReduce on Hadoop Cluster

workspace/python/mapper.py: Mapper script for MapReduce  
workspace/python/reducer.py: Reducer script for MapReduce  
workspace/python/valid_rating_count.py: Python script for conventional method  

workspace/base_output: Output of conventional method on Python  
workspace/hive_output: Final output of Apache Hive (After concatenation)  
workspace/output: Output of MapReduce on local machine  
