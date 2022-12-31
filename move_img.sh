#!/bin/bash

for i in {0..200};do
	mv fig${i}.png ./images/fig${i}.png
done

exit 0