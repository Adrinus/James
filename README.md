# James
A simple text-to-speech speech-to-text chat bot for Linux running python.

## You will need the following Dependencies:

MPlayer

Python

Python-pip

Python-PyAudio

FLAC

SpeechRecognition

eSpeak

chatterbotapi (included)


## On debian based builds:

### Get the requirements:
sudo apt-get install mplayer python python-pip python-pyaudio flac espeak

sudo pip install SpeechRecognition

### Run the program:
Then simply run 'sudo python james.py'

### Errors:
If it spams you with error code but still works fine, just append 2>/dev/null to the end of the command:

'sudo python james.py 2>/dev/null'
