from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.header = "TARS Admin Panel"
admin.site.title = "TARS Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('research/', include('research.urls')),
    path('events/', include('events.urls')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
