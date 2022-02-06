from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name = "Home"),
    path('about/', views.about, name = "About"),
    path('contact/', views.contact, name = "Contact"),
    path('recruitment/', views.recruitment, name = "recruitment")

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
