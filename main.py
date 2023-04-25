import asyncio
import os
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")
r = sr.Recognizer()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

async def getResponse(message):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    return response
 
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

count = 0    
while(1):   
    try:

        with sr.Microphone() as source2:
            if (count == 0):
                print(f"{bcolors.WARNING}Adjusting ambient noise for better sound quality...{bcolors.ENDC}")
                r.adjust_for_ambient_noise(source2, duration=0.2)
            
            print('\n')
            count = 1
            
            audio2 = r.listen(source2)
            ready = f"{bcolors.OKGREEN}I am now ready to listen!{bcolors.ENDC}"
            print(ready)
            SpeakText(ready)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            print('\n')

            print(f"{bcolors.OKGREEN}User: ",MyText,bcolors.ENDC)
            
            print('\n')

            SpeakText(getResponse(MyText))
            print(f"{bcolors.OKBLUE}Response: ", getResponse(MyText), bcolors.ENDC)

    except sr.RequestError as e:
        print(f"{bcolors.FAIL}Could not request results; {0} {bcolors.ENDC}".format(e))
         
    except sr.UnknownValueError:
        print(f"{bcolors.FAIL}unknown error occurred{bcolors.ENDC}")