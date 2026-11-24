
from django.shortcuts import render
from django.conf import settings
from .forms import AudioFileForm
import os
import requests
import time

UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
API_KEY_ASSEMBLYAI = getattr(settings, "API_KEY_ASSEMBLYAI", None) or os.environ.get("API_KEY_ASSEMBLYAI")
CHUNK_SIZE = 5_242_880
HEADERS_AUTH_ONLY = {"authorization": API_KEY_ASSEMBLYAI}
HEADERS = {"authorization": API_KEY_ASSEMBLYAI, "content-type": "application/json"}

def upload(filename):
    def read_file(filename):
        with open(filename, "rb") as audio:
            while True:
                data = audio.read(CHUNK_SIZE)
                if not data:
                    break
                yield data
    response = requests.post(UPLOAD_ENDPOINT, headers=HEADERS_AUTH_ONLY, data=read_file(filename), timeout=120)
    response.raise_for_status()
    return response.json()["upload_url"]

def transcribe(audio_url):
    transcript_request = {
        "audio_url": audio_url,
        "speech_models": ["assemblyai-stt-3-7", "universal-2"],
        "language_detection": True
    }
    response = requests.post(TRANSCRIPT_ENDPOINT, json=transcript_request, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.json()["id"]

def poll(transcript_id):
    polling_endpoint = f"{TRANSCRIPT_ENDPOINT}/{transcript_id}"
    response = requests.get(polling_endpoint, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.json()

def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    start_time = time.time()
    max_wait_time = 900
    while time.time() - start_time < max_wait_time:
        data = poll(transcript_id)
        if data["status"] == "completed":
            return data, None
        elif data["status"] == "error":
            return None, data.get("error", "Transcription failed")
        time.sleep(3)
    return None, "Transcription timed out"

def save_transcript(audio_url, title):
    try:
        data, error = get_transcription_result_url(audio_url)
        if error:
            print("Transcription Error:", error)
            return None
        if data:
            transcripts_dir = os.path.join(settings.MEDIA_ROOT, "transcripts")
            os.makedirs(transcripts_dir, exist_ok=True)
            filename = os.path.join(transcripts_dir, f"{title}.txt")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(data.get("text") or "")
            return filename
    except requests.exceptions.RequestException as error:
        print("AssemblyAI API Error:", error)
    except Exception as error:
        print("Unexpected Error:", error)
    return None

def landing_page(request):
    return render(request, "audioapp/landing_page.html")

def upload_page(request):
    context = {}
    if request.method == "POST":
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                audio_file = form.save()
                audio_url = upload(audio_file.audio.path)
                transcript_filename = save_transcript(audio_url, f"transcript_{audio_file.id}")
                if transcript_filename:
                    with open(transcript_filename, "r", encoding="utf-8") as file:
                        transcript_text = file.read()
                    audio_file.transcript = transcript_text
                    audio_file.save()
                    context["transcription"] = transcript_text
                else:
                    context["transcription"] = "Error in transcription. Please try again."
            except Exception as error:
                print("Upload Error:", error)
                context["transcription"] = "Something went wrong while processing audio."
    else:
        form = AudioFileForm()
    context["form"] = form
    return render(request, "audioapp/upload_page.html", context)

def record_page(request):
    context = {}
    if request.method == "POST" and "audio" in request.FILES:
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                audio_file = form.save()
                audio_url = upload(audio_file.audio.path)
                transcript_filename = save_transcript(audio_url, f"transcript_{audio_file.id}")
                if transcript_filename:
                    with open(transcript_filename, "r", encoding="utf-8") as file:
                        transcript_text = file.read()
                    audio_file.transcript = transcript_text
                    audio_file.save()
                    context["transcription"] = transcript_text
                else:
                    context["transcription"] = "Error in transcription. Please try again."
            except Exception as error:
                print("Recording Error:", error)
                context["transcription"] = "Something went wrong while processing audio."
        else:
            context["form"] = form
    else:
        form = AudioFileForm()
    context["form"] = form
    return render(request, "audioapp/record_page.html", context)
