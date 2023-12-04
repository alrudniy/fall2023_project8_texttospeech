# To be included in Django with the directory myapp/views.py

from django.http import HttpResponse
from django.shortcuts import render
import os

from google.cloud import texttospeech
from playsound import playsound

def text_to_speech(request):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    text_input = "Hello, World!"
    # file_input = os.path.join(file.txt)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=text_input),
        voice=voice,
        audio_config=audio_config
    )

    # The response's audio_content is binary.
    mp3_file_path = os.path.join('media', 'output.mp3')
    with open(mp3_file_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    
    # Play the sound
    playsound(mp3_file_path)

    return HttpResponse('Text-to-speech completed.')

