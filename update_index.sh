#!/bin/sh
python3 parse_repo_json.py | sort >index_body._md
cat index_head._md index_body._md index_tail._md >index.md
