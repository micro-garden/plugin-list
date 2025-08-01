#!/bin/sh
./search.sh
./update_index.sh
./update_categorized.sh
./force-update.sh
./clean-orphan-html.sh
