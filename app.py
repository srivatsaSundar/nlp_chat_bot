from cgitb import text
import json
import os
from typing_extensions import Self
from unittest import result
from urllib import response
from flask import Flask, render_template,url_for, request
import nlp_chat_bot.neuralintents as neuralintents
from nlp_chat_bot.functions import mappings
import pyttsx3
from nlp_chat_bot.preprocesser import chatbot_response

def say_output(audio):
   engine = pyttsx3.init('sapi5')
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate-75)
   engine.say(audio)
   engine.runAndWait()
     
app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/test',methods=["POST"])
def chatbotResponse():
    output = request.get_json()
    message = json.loads(output)  # type: ignore
    print(message.get('spokenwords'))
    speaks=message.get('spokenwords')
    results =chatbot_response(speaks)
    print(results)
    say_output(results)
    return render_template('index.html',results=results)

if __name__ == "__main__":
    app.run(debug=True)