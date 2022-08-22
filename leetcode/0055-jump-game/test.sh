#!/bin/sh

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${SCRIPT_DIR}/..

#set -x
# failing to specify leetcode dir but whatevs
yarn test `basename ${SCRIPT_DIR}`
