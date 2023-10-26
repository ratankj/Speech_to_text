import speech_recognition as sr
from exception import CustomException
from logger import logging

def convert_audio_to_text(audio_path):

    r =sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)


        try:
            text =r.recognize_google(audio)

            return text
        
        except sr.UnknownValueError:
            return "could not understand the audio , not in english language"
        
        except sr.RequestError as e:
            return f"could not request result ; {e}"

