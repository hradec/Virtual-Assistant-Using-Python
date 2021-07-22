
IF NOT EXIST "wenv" (
	python3 -m venv wenv
        wenv\Scripts\pip install pipwin
        wenv\Scripts\pip install SpeechRecognition gtts wikipedia 
        wenv\Scripts\pipwin install pyaudio
) 
wenv\Scripts\python google-voiceattack-win.py
