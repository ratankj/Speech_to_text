import os,sys
from flask import Flask,render_template,redirect,request
from utils.utils import convert_audio_to_wav , allowed_file
from utils.text_to_speech import convert_audio_to_text
from exception import CustomException
from logger import logging


try:
    app = Flask(__name__)

    UPLOAD_FOLDER = "uploads"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    path = os.path.abspath("app.config['UPLOAD_FOLDER']")
    print(f"pathh location is {path}")
    logging.info(f"test data path, {path}")


    def create_upload_directory():
        
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            print(f"{(app.config['UPLOAD_FOLDER'])} does not exist.")
            os.makedirs(app.config['UPLOAD_FOLDER'])
            logging.info(f"test data path, {(app.config['UPLOAD_FOLDER'])}")
            
                
        else:
            print(f"{(app.config['UPLOAD_FOLDER'])} exists.")
            logging.info(f"test data path, {(app.config['UPLOAD_FOLDER'])}")
            


    @app.route('/',methods = ['GET','POST'])
    def index():
        if request.method == 'POST':
            create_upload_directory()
            logging.info(f"checking the file create upload history")

            if 'audio_file' not in request.files:
                return redirect(request.url)
            

            file = request.files['audio_file']
            logging.info(f" file path is : {file}")

            if file.filename == "":
                return redirect(request.url)
            
            if file and allowed_file(file.filename):
                audio_path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)

                logging.info(f"audio file path is : {audio_path}")
                file.save(audio_path)

                # convert audio to wav
            wav_path = convert_audio_to_wav(audio_path)
            logging.info(f"wav  file path is : {wav_path}")

                # convert wav data to text function
            text =  convert_audio_to_text(wav_path)
            logging.info(f"text  file path is : {text}")
            
            return render_template('index.html',text=text)
        
        return render_template('index.html',text=None)

    if __name__ == '__main__':
        app.run(debug = True)
            

except Exception as e:
    logging.info("in app file")
    raise CustomException(e,sys)