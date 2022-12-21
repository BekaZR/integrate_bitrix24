from django.urls import path

from mainapp.views import linkview

urlpatterns = [
    path("", linkview)
]