#!/bin/bash

clear

python3 nest.py | sed 's/\\n//g;s/b//g'
