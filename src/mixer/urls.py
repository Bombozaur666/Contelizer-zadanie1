from django.urls import path

from .views import UploadView, ResultView

urlpatterns = [
    path("", UploadView.as_view(), name="mixer-upload"),
    path("preview/", ResultView.as_view(), name="mixer-preview"),
]