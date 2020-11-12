#!/usr/bin/env bash
set -xv
echo "Error message collected from the last failed node"

hdfs dfs -mkdir -p ${1}

appId=$(echo ${2} | sed "s/Application \(.*\) finished with FAILED status/\1/")

yarn logs -applicationId ${appId} -log_files stdout | hdfs dfs -put -f - ${1}/${3}_${appId}.log
