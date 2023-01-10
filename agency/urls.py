from django.urls import path

from .views import index

from .views import (
    index,
)

urlpatterns = path("", index, "index"),
