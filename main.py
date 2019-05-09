from text2speech import TextToSpeech
import os

key = os.environ['SPEECHKEY']

# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech

t2s = TextToSpeech(key, 'en-US-JessaNeural')

# t2s = TextToSpeech(key)

t2s.play(" Hello, and welcome to Bits of Build. ")
t2s.play(" I scanned a delicious apple.")
