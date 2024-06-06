#!/bin/bash

set -e

python predict/data.py
python predict/train.py

python level/data.py
python level/train.py