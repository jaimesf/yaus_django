# -*- encoding: utf-8 -*-
from django.conf.urls import include, url
from django.conf.urls.static import static
from yaus import settings

urlpatterns = [
    url(r'^', include('web.urls', namespace="public")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


