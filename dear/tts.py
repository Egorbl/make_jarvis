import os
from playsound import playsound
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

def prepare_text(text):
    escaped_text = text.replace('"', '\\"')
    return escaped_text

def say(text):
    load_dotenv()
    openai_key = os.getenv('OPENAI_KEY')
    client = OpenAI(base_url="https://api.proxyapi.ru/openai/v1/", api_key=openai_key)
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )

    response.stream_to_file(speech_file_path)
    playsound(speech_file_path)

def do_tts(text):
    say(text)

def interrupt_tts():
    os.system('killall say')
