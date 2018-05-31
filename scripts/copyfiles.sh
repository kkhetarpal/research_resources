#!/bin/sh

for idx in $(seq 901 2000)
do
    filename="frame$idx.jpg"
    echo $filename
    mv $filename /home/ml/kkheta2/sam/sample_images
done
exit 0
