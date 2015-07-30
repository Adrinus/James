from chatterbotapi import ChatterBotFactory, ChatterBotType
import speech_recognition as sr
import sys
import subprocess
r = sr.Recognizer()
r.energy_threshold = 4000
r.dynamic_energy_threshold = True
factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

user_input = "Say something to begin..."

print(user_input)

while True:
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout = None)
        try:
                user_input = r.recognize(audio)
                print("User: " + user_input)
        except LookupError:
                print("Could not understand  you")

        s = bot1session.think(user_input);
        subprocess.call('espeak -k 20 -s 140 -v en-rp+m7 "{0}" 2>/dev/null' .fo$
        print 'James: ' + s
