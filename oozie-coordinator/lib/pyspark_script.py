#!/usr/bin/env python3
"""
PySpark template script.
"""
import argparse
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import IntegerType, FloatType
import pyspark.sql.functions as F


# Create session
spark = SparkSession.builder.appName("App name").getOrCreate()
# Add directory or file to path
spark.sparkContext.addFile("hdfs://<hostname>:8020/<path>/dir", recursive=True)
spark.sparkContext.addPyFile("hdfs://<hostname>:8020/<path>/file1.py")
# Import stuff from this path
import dir.module1 as m
import file1
# Get SQLContext
sqlCtxt = SQLContext(spark.sparkContext)


if __name__='__main__':
    # Retrieve arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("argument_1", help="description 1")
    parser.add_argument("argument_2", help="description 2")
    parser.add_argument("argument_3", help="description 3")
    args = parser.parse_args()
    arg1 = args.argument_1
    arg2 = args.argument_2
    arg3 = args.argument_3
    # Do stuff
