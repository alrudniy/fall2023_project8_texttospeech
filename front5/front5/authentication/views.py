from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first = request.POST['firstname']
        last = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myUser = User.objects.create_user(username, email, pass1)
        myUser.first_name=first
        myUser.last_name=last
        myUser.save()

        messages.success(request, "Account Profile successfully created. :D")
        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            first = user.first_name
            return render(request, "authentication/index.html",{'firstname':first})

        else:
            messages.error(request, 'Error: Invalid Credentials')
            return redirect(home)


    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "logout successful")
    return redirect('home')

def mainapp(request):
    return render(request, 'authentication/mainapp.html')

def history(request):
    return render(request, 'authentication/history.html')

def profile(request):
    return render(request, 'authentication/profile.html')

# To be included in Django with the directory myapp/views.py


#from django.http import HttpResponse
#from django.shortcuts import render
import os
import json
from django.http import JsonResponse
from google.cloud import texttospeech
from playsound import playsound
from datetime import datetime

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

    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "output_" + date_string + ".mp3"
    mp3_file_path = os.path.join(filename)

    # The response's audio_content is binary.
    #mp3_file_path = os.path.join('media', 'output.mp3')
    with open(mp3_file_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    
    # Play the sound
    playsound(mp3_file_path)

    #return HttpResponse('Text-to-speech completed.')
    return render(request, 'authentication/mainapp.html')