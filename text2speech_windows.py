from azure_text_speech import AzureSpeechServices
import time
import hashlib
from pathlib import Path
import os
from datetime import datetime
from pygame import mixer
import wave
import io


class TextToSpeech():
    def __init__(self, azureSpeechServiceKey, voice='en-US-GuyNeural', enableMemCache=False, enableDiskCache=False):
        self.text2Speech = AzureSpeechServices(azureSpeechServiceKey, voice)
        self.voice = voice
        self.enableMemCache = enableMemCache
        self.enableDiskCache = enableDiskCache

        self.ttsAudio = {}

        self.startSoundTime = datetime.min
        self.soundLength = 0.0

        mixer.pre_init(frequency=16000, size=-16, channels=1)

        if not Path('.cache-audio').is_dir():
            os.mkdir('.cache-audio')

    def play(self, text):
        if text is None or text == '':
            return

        digestKey = hashlib.md5(text.encode()).hexdigest()

        audio = self.ttsAudio.get(digestKey) if self.enableMemCache else None

        if audio is None:
            cacheFileName = "{}-{}.wav".format(
                self.voice, digestKey)

            cacheFileName = os.path.join('.cache-audio', cacheFileName)

            if self.enableDiskCache and Path(cacheFileName).is_file():
                with open(cacheFileName, 'rb') as audiofile:
                    audio = audiofile.read()
            else:
                audio = self.text2Speech.get_audio(text)
                if audio is None:
                    print(
                        'Text to Speech problem: Check internet connection or Speech key')
                    return

                if self.enableDiskCache and audio is not None:
                    with open(cacheFileName, 'wb') as audiofile:
                        audiofile.write(audio)
            if self.enableMemCache:
                self.ttsAudio[digestKey] = audio
        
        
        mixer.init()
        
        self.sound = mixer.Sound(audio)
        self.sound.play()
        time.sleep(self.sound.get_length())

        mixer.quit()
