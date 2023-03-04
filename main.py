import speech_recognition as sr
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# create a recognizer object
recognizer = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone(0) as source:
    print("Katakan sesuatu")
    # adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    # record audio from the microphone
    audio = recognizer.listen(source)

    # recognize speech using Google Speech Recognition in Indonesian language
    try:
        text = recognizer.recognize_google(audio, language="id-ID")
        # Print the transcript
        print("Permintaan anda:", text)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5
        )

        print(response.choices[0].text)
    except sr.UnknownValueError:
        print("Maaf, saya tidak mengerti apa yang anda katakan")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
