#!/bin/sh
cat index_body._md | ./categorize.pl >categorized_body._md
cat categorized_head._md categorized_body._md categorized_tail._md >categorized.md
