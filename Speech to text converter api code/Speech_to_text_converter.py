import speech_recognition as sr
from flask import Flask, jsonify, request
import os

i=True

app = Flask(__name__)

r=sr.Recognizer()
audio = 'genevieve.wav'

@app.route('/sttc')
def speech_to_text():
    with sr.AudioFile(audio) as source:
        r.adjust_for_ambient_noise(source)
        converted_audio = r.listen(source)
        text = r.recognize_google(converted_audio)

    file = open('Text.txt', 'w+')
    if i:
        file.write(str(text))
    file.close()

    os.remove('genevieve.wav')
    
    return jsonify({"Conversion Successful":"Your Speech has successfully been converted to text and added to Text.txt in the given directory"})

app.run(port=5100)
