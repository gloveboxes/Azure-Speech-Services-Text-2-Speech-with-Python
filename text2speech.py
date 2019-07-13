from azure_speech import AzureSpeechServices
# import pyaudio
# import wave
# import sys
# import io
from pygame import mixer
import time



class TextToSpeech():
    # Short name for 'Microsoft Server Speech Text to Speech Voice (en-US, GuyNeural)'
    def __init__(self, azureSpeechServiceKey, voice='en-US-GuyNeural'):
        self.translator = AzureSpeechServices(azureSpeechServiceKey, voice)
        self.ttsAudio = {}
        mixer.init(frequency=16000, size=-16, channels=1)

    # def _playAudio(self, audio):
    #     CHUNK = 1024

    #     f = io.BytesIO()
    #     f.write(audio)
    #     f.seek(0)
    #     wf = wave.Wave_read(f)

    #     print(wf.getframerate())
    #     print(wf.getsampwidth())

    #     p = pyaudio.PyAudio()

    #     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                     channels=wf.getnchannels(),
    #                     rate=wf.getframerate(),
    #                     output=True)

    #     data = wf.readframes(CHUNK)

    #     while data != b'':
    #         stream.write(data)
    #         data = wf.readframes(CHUNK)

    #     stream.stop_stream()
    #     stream.close()
    #     p.terminate()

    def play(self, text):
        text = text.lower()
        audio = self.ttsAudio.get(text)
        if audio == None:
            print('audio not found')
            audio = self.translator.get_audio(text)

            # audio = self.translator.speak(
            #     text, "en-AU", "Catherine", "riff-16khz-16bit-mono-pcm")
            self.ttsAudio[text] = audio

        self.sound = mixer.Sound(audio)
        self.sound.play()
        while mixer.get_busy():
            time.sleep(0.25)
        # self._playAudio(audio)
