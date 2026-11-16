#!/bin/bash

set -e

cd -- "$(dirname -- "$0")"
echo "----- Calculator quality gate -----"
python -m pytest -v
echo "QUALITY GATE PASSED"
