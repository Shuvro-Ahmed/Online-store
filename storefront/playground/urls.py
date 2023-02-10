from django.urls import URLPattern, path
from . import views

#urlConf
urlpatterns = [
    path('hello/', views.hello)
]