from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.eventshome, name = "eventshome"),
    path('register/', views.eventregister, name = "eventregister"),
    path('<str:slug>', views.eventsingle, name = "eventsingle")

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
