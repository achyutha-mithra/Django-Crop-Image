from django.urls import path
from . import views

urlpatterns = [
    path("image_view", views.image_view, name="image_view")
]
