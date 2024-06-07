#!/bin/bash

set -e

python data.py
python predict/train.py

python level/train.py