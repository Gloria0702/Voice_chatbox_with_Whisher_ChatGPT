import gradio as gr
import os
from pathlib import Path
import openai, config, subprocess
from win32com.client import Dispatch
import audio_recorder
import re
openai.api_key = config.OPENAI_API_KEY


messages = [{"role": "system", "content": '""I want you to act as a career counselor. '
                                          'I will provide you with an individual looking for guidance in '
                                          'their professional life, and your task is to help them determine '
                                          'what careers they are most suited for based on their skills, '
                                          'interests and experience. You should also conduct research into '
                                          'the various options available, explain the job market trends in '
                                          'different industries and advice on which qualifications would be '
                                          'beneficial for pursuing particular fields. '
                                          'My first request is: '
                                          'I want to advise someone who wants to pursue a potential career in software engineer."""'
}]



import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time} seconds")
        return result
    return wrapper

@time_it##calculate the running time for the overall process
def transcribe(audio):
    global messages
    # audio = audio.replace('\\', '\\\\')
    #print(audio_new_name)
    audio_file = open(audio, "rb")#audio_file = open(audio_new_name, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript["text"])
    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)
    print(system_message['content'])

    # -------Speak with MacOS------------
    # subprocess.call(["say", system_message['content']])#for MacOS
    #-------Speak with Win10 OS----------
    speaker = Dispatch('SAPI.SpVoice')
    speaker.Voice = speaker.GetVoices().Item(1)
    speaker.Speak(system_message['content'])

    # -----------------------------------

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return system_message['content']

# ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
# ui.launch()


play = True

while play:
    audio = audio_recorder.record_audio()
    transc = transcribe(audio)
