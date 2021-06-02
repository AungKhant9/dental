from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('pricing.html', views.pricing, name="pricing"),
    path('contact.html', views.pricing, name="contact"),
]
