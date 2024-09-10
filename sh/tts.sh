#!/bin/sh

CURRENT_DIR=$(pwd)
cd $TTSUTILITIES
source venv/bin/activate
python src/tts.py "$CURRENT_DIR/$1" "$2"
deactivate
