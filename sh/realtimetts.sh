#!/bin/sh

cd $TTSUTILITIES
source venv/bin/activate
python src/realtimetts.py
deactivate
