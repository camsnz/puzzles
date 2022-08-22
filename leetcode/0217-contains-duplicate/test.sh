#!/bin/sh

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

#set -x
# failing to specify leetcode dir but whatevs
python3 ${SCRIPT_DIR}/ContainsDuplicate.test.py
