import asyncio
import os
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")
r = sr.Recognizer()

async def getResponse(message):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    print("User: \n" + message)
    return response
 
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
      
while(1):   
    try:

        with sr.Microphone() as source2:
             
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            audio2 = r.listen(source2)
             
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("User: ",MyText)
            SpeakText(getResponse(MyText))
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")