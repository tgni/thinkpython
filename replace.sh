#!/bin/bash

new=/tmp/overwr1.$$
echo "replace $1 as $2..."
for i in `find . -name "*.py" -print`
do
	echo "modify $i..."

	sed "s/$1/$2/g" $i > $new
	cp $new $i
done

