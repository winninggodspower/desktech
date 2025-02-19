from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("training", views.training, name="training"),
    path("job", views.job, name="job"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
