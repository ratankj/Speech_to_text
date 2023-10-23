import os,sys
from pydub import AudioSegment
ALLOWED_EXTENTIONS = {'mp3','wav'}

def convert_audio_to_wav(audio_path):
    sound = AudioSegment.from_mp3(audio_path)
    wav_path = audio_path.replace('.mp3','.wav')

    sound.export(wav_path, format = "wav")

    return wav_path

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS