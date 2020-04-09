#!/bin/bash

source ${DIR}bin/activate

OUTPUT=$(python3 ${DIR}chatbot.py)
echo -e "\n"$OUTPUT"\n"

