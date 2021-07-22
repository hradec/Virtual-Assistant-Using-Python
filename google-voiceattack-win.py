import speech_recognition as sr
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import webbrowser

# ignore any warnings messages
warnings.filterwarnings('ignore')

# Record audio and return it into String
def recordAudioAsString():
    # Record the audio
    r = sr.Recognizer()
    # Open microphone& start recording
    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)

    # Use google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError:
        print('We cannot understand the audio, unknown error')
    # In case if service is disconnected
    except sr.RequestError as e:
        print('Service Error '+e)

    return data

def getAlexaResponse(inputCommandText):
    print(inputCommandText)
    # Convert text to speech
    obj = gTTS(text=inputCommandText, lang='en', slow=False)
    obj.save('alexa_response.mp3')
    # Play the response file
    try:
      import vlc
      p = vlc.MediaPlayer('file://%s' % os.path.abspath('alexa_response.mp3'))
      p.play()
    except: pass
    import subprocess
    subprocess.call([
	'C:/Program Files (x86)/VoiceAttack/VoiceAttack.exe',
	'-command',
	'%s' %  inputCommandText
    ])

def iceBreakingWords(text):
    words = ['Hey Anuja, how may I help you', 'Okay Anuja', 'Alexa welcomes you']

    for w in words:
        if text in text:
            return True

    return False

def getDate():

    now = datetime.datetime.now()
    current_date = datetime.datetime.today()
    current_day = calendar.day_name[current_date.weekday()]
    month = now.month
    day = now.day

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
    ordinal_list = [ordinal(n) for n in range(1,32)]

    return 'Today is '+current_day+' '+month_list[month-1]+' '+ordinal_list[day-1]

def greet(text):

    inputGreetWords = ['hi', 'hello']
    outputGreetWords = ['Hello, how can I help you?', 'Hey, wassup']

    for word in text.split():
        if word in inputGreetWords:
            return random.choice(outputGreetWords)

    return text #' '

def getPersonData(text):

    text_list = text.split()
    # print(text_list)
    for i in range(0,len(text_list)):
        if i<=len(text_list) and text_list[i].lower()=='who' and text_list[i+1].lower()=='is':
            # print(text_list[2]+ ' '+text_list[3])
            return text_list[2]+ ' '+text_list[3]

while True:
    text = recordAudioAsString()
    response = ''

    if greet(text):
        response = response + greet(text)

        if 'date'  in text:
            get_date = getDate()
            response = response +' '+ get_date

        if 'who is' in text:
            person = getPersonData(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response+' '+ wiki

        getAlexaResponse(response)
