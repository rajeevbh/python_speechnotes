from django.shortcuts import render
from .speech_recognizer import recognize_speech_from_mic

def home(request):
    transcription = None
    if request.method == 'POST':
        transcription = recognize_speech_from_mic()
    return render(request, 'speechapp/home.html', {'transcription': transcription})
