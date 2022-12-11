import logging

import youtube_dl

from django.core.mail import send_mail

from videoconverteronline.celery import app
from videoconverteronline.settings import EMAIL_HOST_USER

from .models import Convert
from .service import VideoConverterService

logger = logging.getLogger(__name__)


@app.task
def convert_and_send(convert_id: int):
    try:
        convert = Convert.objects.get(pk=convert_id)
    except Convert.DoesNotExist:
        logger.error('convert with id %s doesnot exist', convert_id)
        return

    service = VideoConverterService(convert)
    download_link = service.download()
    if download_link:
        service.send()
