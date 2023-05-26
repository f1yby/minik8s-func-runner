#!/usr/bin/env bash

echo "$_PRE_RUN" | base64 -d >pre_run.sh
echo "$_FUNC" | base64 -d >func.py

bash pre_run.sh
echo "[pre_run] OK"
python main.py
echo "[main] OK"
sleep 10
