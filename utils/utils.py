import os,sys
from pydub import AudioSegment
from exception import CustomException
from logger import logging

try:
    ALLOWED_EXTENTIONS = {'mp3','wav'}

    logging.info(f"test data path, {ALLOWED_EXTENTIONS}")

    def convert_audio_to_wav(audio_path):
        sound = AudioSegment.from_mp3(audio_path)
        wav_path = audio_path.replace('.mp3','.wav')

        logging.info(f"test data path, {wav_path}")

        sound.export(wav_path, format = 'wav')

        return wav_path




    def allowed_file(filename):
        check_result = '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS
        print(f"print this {'.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS}")
        print(f"the result of this is : {check_result}")
        logging.info(f"test data path, {check_result}")
        
        return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS
    
    
except Exception as e:
            logging.info("in utils.py file")
            raise CustomException(e,sys)
    
