from google.cloud import texttospeech
from playsound import playsound

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Function to read text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Set the file path for the text input
input_file_path = "input_text.txt"

# Read text from the file
text_content = read_text_from_file(input_file_path)

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text_content)

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
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
output_file_path = "output.mp3"
with open(output_file_path, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print(f'Audio content written to file "{output_file_path}"')
