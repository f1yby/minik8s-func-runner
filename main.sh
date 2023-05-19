#!/usr/bin/env bash

wget -O pre_run.sh $_PRE_RUN
wget -O func.py $_FUNC

bash pre_run.sh

python main.py