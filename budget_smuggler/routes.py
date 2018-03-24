from django.conf.urls import include, url
from rest_framework import urls as rest_framework_urls

urlpatterns = [
    url(r'^backend/api/v1/', include(rest_framework_urls)),
]
