#!/usr/bin/env bash

wget -O pre_run.sh $_PRE_RUN
wget -O func.py $_FUNC

bash pre_run.sh
echo "[pre_run] OK"
python main.py
echo "[main] OK"