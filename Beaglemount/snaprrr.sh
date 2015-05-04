#!/bin/bash

TSTAMP=`date +%s`
STREAM=/usr/bin/streamer

mkdir -p fileoutput
FILE=fileoutput/filezz${TSTAMP}.jpeg
CROP_FILE=${FILE}_CROP.png
CHAN_FILE=${FILE}_CHAN
SPEC_FILE=${FILE}_SPECTRUM.png
LINE_FILE=${FILE}_LINE.bin


echo "Bzzzt.. taking a sip to pickkk.. ${FILE}"
${STREAM} -o ${FILE} -s 480x180
ls -la ${FILE}


echo "Bzuuerp, croppin' that bad b0y into ${CROP_FILE}..."
convert -crop 1280x180+0+230! -quality 100  ${FILE} ${CROP_FILE}

echo "ssszzzirrrup, separatin' ze colors..."
convert -separate ${CROP_FILE} ${CHAN_FILE}%d.png

echo "buuuuurp, adding pixels back-to-getherz.."
convert -compose plus ${CHAN_FILE}0.png ${CHAN_FILE}1.png -composite ${CHAN_FILE}2.png -composite $SPEC_FILE


echo "Mo' croppingzz"
convert -crop 1280x1+0+83! -quality 100  ${SPEC_FILE} gray:${LINE_FILE}
