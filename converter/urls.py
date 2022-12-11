from django.urls import path
from . import views

urlpatterns = [
    path("", views.ConvertView.as_view(), name="convert"),
]
