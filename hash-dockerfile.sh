#!/bin/bash
echo -e "FROM python3 \nRUN pip install numpy scipy pandas \nCMD [\""python"\", ./main.py]" > Dockerfile

cat Dockerfile

HASH_OUTPUT=$(sha1sum Dockerfile)

echo $HASH_OUTPUT





