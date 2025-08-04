#!/bin/sh
./search.sh
./update-index.sh
./update-categorized.sh
./force-update.sh
./clean-orphan-html.sh
