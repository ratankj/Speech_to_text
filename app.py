import os,sys
from flask import Flask,render_template,redirect,request
from utils.utils import convert_audio_to_wav , allowed_file
from utils.text_to_speech import convert_audio_to_text


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_upload_directory():
    if not os.path.exist(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        create_upload_directory()

        if 'audio_file' not in request.files:
            return redirect(request.url)
        

        file = request.file['audio_file']

        if file.filename == "":
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            audio_path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
            file.save(audio_path)

            # convert audio to wav
            wav_path = convert_audio_to_wav(audio_path)

            # convert wav data to text function
            text =  convert_audio_to_text(wav_path)
            return render_template()