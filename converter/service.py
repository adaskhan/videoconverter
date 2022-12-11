import youtube_dl

from django.core.mail import send_mail

from videoconverteronline.settings import EMAIL_HOST_USER

from .models import Convert


class VideoConverterService:

    def __init__(self, converter: Convert):
        self.convert = converter

    def send(self):
        user_email = self.convert.email
        message = 'Здесь будет ссылка. {}'
        if self.convert.local_url:
            message = message.format(self.convert.local_url)
        else:
            message = message.format('Пока что ссылка не сгенерирована')

        send_mail(
            subject='Ссылка на скачивание видео в формате mp3',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user_email, ]
        )

    def download(self):
        link = self.convert.yt_url
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
            'keepvideo': True,
            'nocheckcertificate': True,
            'logtostderr': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        # снегерировать url

        # сохранить в бд / google drive api

        # self.convert.set_local_url(some_url)

        # return some_url
