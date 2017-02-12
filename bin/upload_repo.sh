#!/bin/sh

NEXUS_HOST=10.42.0.42

TOP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/..

cd $TOP_DIR/repo_artifacts

find . ! -path . | while read line; do
  FILE=$line
  curl -v --fail -u admin:admin123 --upload-file $FILE http://$NEXUS_HOST:8081/repository/demo/store/1.0.0/$FILE 
done

