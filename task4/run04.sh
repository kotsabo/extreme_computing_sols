hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapred.reduce.tasks=1 -files mapper04.py,reducer04.py -input /data/assignments/ex2/part3/webLarge.txt -output /user/s1736880/assignment2/task4 -mapper mapper04.py -reducer reducer04.py
