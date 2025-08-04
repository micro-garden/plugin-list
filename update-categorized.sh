#!/bin/sh
cat index-body._md | ./categorize.pl >categorized-body._md
cat categorized-head._md categorized-body._md categorized-tail._md >categorized.md
