
from azure_text_translate import AzureTranslationServices
import hashlib
from pathlib import Path
import os
from datetime import datetime
import io


class TextTranslation():
    def __init__(self, azureTranslatorServiceKey=None, translateToLanguage=None, enableMemCache=False, enableDiskCache=False):
        self.initialized = False
        if azureTranslatorServiceKey is None or translateToLanguage is None:
            print('Azure Translate Service Key and To Language Values Required')
            return 
        
        self.initialized = True

        self.translateText = AzureTranslationServices(
            azureTranslatorServiceKey, translateToLanguage)

        self.azureTranslatorServiceKey = azureTranslatorServiceKey
        self.translateToLanguage = translateToLanguage

        self.enableMemCache = enableMemCache
        self.enableDiskCache = enableDiskCache

        self.translated_text = {}

        if not Path('.cache-text').is_dir():
            os.mkdir('.cache-text')

    
    def translate(self, text):
        if not self.initialized or text is None or text == '':
            return

        digestKey = hashlib.md5(text.encode()).hexdigest()

        translatedText = self.translated_text.get(digestKey) if self.enableMemCache else None

        if translatedText is None:
            cacheFileName = "{}-{}.wav".format(self.translateToLanguage, digestKey)

            cacheFileName = os.path.join('.cache-text', cacheFileName)

            if self.enableDiskCache and Path(cacheFileName).is_file():
                with open(cacheFileName, 'r', encoding="utf-8") as textfile:
                    translatedText = textfile.read()
            else:
                translatedText = self.translateText.translate(text)
                if translatedText is None:
                    print('Text translation error: Check internet connection,Translation key, or language')
                    
                    return None

                if self.enableDiskCache:
                    with open(cacheFileName, 'w', encoding="utf-8") as textfile:
                        textfile.write(translatedText)
            if self.enableMemCache:
                self.translated_text[digestKey] = translatedText

        return translatedText

