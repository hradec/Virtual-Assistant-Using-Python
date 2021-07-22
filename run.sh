#!/bin/bash

if [ ! -e env/bin/activate ] ; then
	python3 -m venv env
	source env/bin/activate
	pip3 install --upgrade pip
	pip3 install \
		SpeechRecognition \
		gtts \
		wikipedia \
		pyaudio \
		python-vlc
fi

source env/bin/activate

python3 $1

source env/bin/deactivate

