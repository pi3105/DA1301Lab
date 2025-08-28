#!/bin/bash
sort numbers.txt
ipconfig getifaddr en0
cat readme.txt
wc -l data.csv
grep -lr error logs/
tail -n10 app.log
chmod a+x script.sh
grep -ir TODO *.py
history 20
ps aux --sort -rss
find / -type d -name backup
sed 's/foo/bar/g' example.txt > new_example.txt
