from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='photos-home'),
    path('about/',views.about, name='photos-about'),
    path('register/',views.about, name='photos-register'),
    path('login/',views.about, name='photos-login'),
]