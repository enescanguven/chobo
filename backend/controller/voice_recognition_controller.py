from deepgram import Deepgram


class VoiceRecognitionController():
    def __init__(self) -> None:
        DEEPGRAM_API_KEY = '5c04c150c3115eb2d3ba52617cddee54eb96fad8'
        self.MIMETYPE = 'm4a'
        self.deepgram = Deepgram(DEEPGRAM_API_KEY)

        pass
    async def get_transcript(self, audio_path):
        audio = open(audio_path, 'rb')
        source = {
        'buffer': audio,
        'mimetype': self.MIMETYPE
        }

        response = await self.deepgram.transcription.prerecorded(source,
        {
            'punctuate': True,
            'language': 'tr'
        })
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript
    
    
voice_recognition_controller = VoiceRecognitionController()
