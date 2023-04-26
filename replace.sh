#!/bin/bash

new=/tmp/overwr1.$$
for i in `find $1 -name "*.py" -print`
do
	echo "modify $i..."

	sed 's/home\/tgni\/ml\/env/usr/g' $i > $new
	cp $new $i
done

