from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.researchhome, name = "researchhome"),
    path('<str:slug>/', views.researchsingle, name = "researchsingle"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
