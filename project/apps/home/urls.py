from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import index

urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += staticfiles_urlpatterns()
