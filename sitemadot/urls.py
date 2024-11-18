from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from  madot.views import home, destination_details, send_contact_email, send_destination_email
from sitemadot import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact', send_contact_email, name='contact'),
    path('destination/<int:id>/', destination_details, name='destination'),
    path('send_destination_email', send_destination_email, name='send')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
