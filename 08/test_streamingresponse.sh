#!/bin/bash
file=$1
python "$file" &
PID=$!
sleep 2

for i in $(seq 0 2); do
    curl -X POST 127.0.0.1:8200/ping &
done

sleep 7
kill -9 $PID
