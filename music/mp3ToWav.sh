#!/bin/sh


files="./*.mp3"

for filepath in ${files}
do
   mpg123 -w "${filepath:2:-4}.wav" "${filepath:2:-4}.mp3"
done
