#!/bin/bash.

curl -s $1 | grep href | cut -c16- | rev | cut -c24- | rev

