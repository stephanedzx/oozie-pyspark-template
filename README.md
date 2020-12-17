# oozie-pyspark-template
Template Oozie - PySpark job

## About coordinator.xml
**timeout** : how long the coordinator action will be in WAITING or READY
status before giving up on its execution, default -1<br>

**concurrency** : How many coordinator actions are allowed to run concurrently 
(RUNNING status) before the coordinator engine starts throttling them, 
default 1<br>

**execution** : Strategy when there is a backlog of coordinator actions in the 
coordinator engine. FIFO (default), LIFO, ONLYLAST<br>

**throttle** : How many maximum coordinator actions are allowed to be in 
WAITING state concurrently, default<br>

In coordinator.xml, "current_date" value is set and given as parameter to the workflow.

## About job.properties 
**HDFS hostname** is found in "oozie-default.xml" > property "fs.defaultFS".<br>

**job tracker** is found in "oozie-default.xml" > property "yarn.resourcemanager.address.rm2".<br>

"oozie-default.xml" is found in Hadoop "conf/" directory, e.g. /etc/hadoop/conf/oozie-default.xml<br>
