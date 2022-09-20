from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generic.urls'), name='home'),
    path('events/', include('events.urls'), name='events'),
    path('specials/', include('specials.urls'), name='specials'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('about_us/', include('about.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
