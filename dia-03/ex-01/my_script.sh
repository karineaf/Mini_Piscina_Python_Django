#!/bin/bash

pip3 --version
pip3 install path.py --target=local_lib --log logs.log
python3 my_program.py
