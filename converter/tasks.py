from videoconverteronline.celery import app
from django.core.mail import send_mail
import youtube_dl
from videoconverteronline.settings import EMAIL_HOST_USER


@app.task
def send_spam_email(user_email):
    send_mail(
        subject='Ссылка на скачивание видео в формате mp3',
        message='Здесь будет ссылка. Я это потом сделаю',
        from_email=EMAIL_HOST_USER,
        recipient_list=[user_email, ]
    )


@app.task
def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
