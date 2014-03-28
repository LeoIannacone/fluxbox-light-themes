#!/bin/bash

function make_icon() {
	TMP=/tmp/btn.png
	NAME=${1}.png
	ICON=${ORIG}/${NAME}
	RESULT=${DEST}/{NAME}
	FOCUS=window_${2}.png
	if [[ $1 == close* ]] ; 	then POSITION="left"; GRAVITY="East"; 	fi
	if [[ $1 == maximize* ]] ; 	then POSITION="right"; GRAVITY="West"; fi
	if [[ $1 == minimize* ]] ; 	then POSITION="middle"; GRAVITY="Center";  fi
	POSITION_IMAGE=${ORIG}/trough_${POSITION}.png
	if [ $POSITION == "middle" ] ; then
 		convert -scale 25x19\! $POSITION_IMAGE $TMP
 		POSITION_IMAGE=$TMP
 	fi
	composite -gravity center  $ICON $POSITION_IMAGE $TMP
	composite -gravity $GRAVITY $TMP $FOCUS $NAME
	rm $TMP
}

function make_theme() {

	cd $1/pixmaps
	for icon in "close" "maximize" "minimize" ; do
		make_icon ${icon} focused
		make_icon ${icon}_focused_pressed focused
		make_icon ${icon}_unfocused unfocused
	done
	cd -

}

for theme in "Ambiance" "Radiance" ; do

	ORIG=/usr/share/themes/${theme}/metacity-1
	make_theme ${theme}

done
