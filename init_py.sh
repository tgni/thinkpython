#!/bin/bash
dirs=`find . \( -path ./.git -o -path ./.project_vim \) -prune -o -type d -print`
for dir in ${dirs}
do
	cd ${dir} && touch __init__.py && cd -
done
