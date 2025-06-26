from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

from root.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.urls')),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
                  path('i18n/set_language/', set_language, name='set_language'),
                  # path('accounts/', include('allauth.urls')),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL, document_root=STATIC_ROOT)
admin.site.site_header = "Alijahon Admin"
admin.site.site_title = "Alijahon Admin Portal"
admin.site.index_title = "Welcome to Alijahon Researcher Portal"
