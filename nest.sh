#!/bin/bash

clear

getNest() {

	python3 nest.py | sed 's/\\n//g;s/b//g'
}

clear
