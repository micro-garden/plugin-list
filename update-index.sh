#!/bin/sh
python3 parse-repo-json.py >index-body._md
cat index-head._md index-body._md index-tail._md >index.md
