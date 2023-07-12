# Example filename: deepgram_test.py

import sys
from deepgram import Deepgram
import asyncio, json

DEEPGRAM_API_KEY = '5c04c150c3115eb2d3ba52617cddee54eb96fad8'

FILE = 'tatli.wav'

MIMETYPE = 'wav'
async def main():

  deepgram = Deepgram(DEEPGRAM_API_KEY)
  if FILE.startswith('http'):
    source = {
      'url': FILE
    }
  else:
    audio = open(FILE, 'rb')
    source = {
      'buffer': audio,
      'mimetype': MIMETYPE
    }

  response = await asyncio.create_task(
    deepgram.transcription.prerecorded(
      source,
      {
        # 'smart_format': True,
        # 'model': 'general',
        'punctuate': True,
        'language': 'tr'

      }
    )
  )


  print(response['results']['channels'][0]['alternatives'][0]['transcript'])


try:
  asyncio.run(main())
except Exception as e:
  exception_type, exception_object, exception_traceback = sys.exc_info()
  line_number = exception_traceback.tb_lineno
  print(f'line {line_number}: {exception_type} - {e}')