from django.conf.urls import include, url
from rest_framework import urls as rest_framework_urls

from . import views

routes = [
    ('expenses', views.ExpenseViewSet),
]

urlpatterns = [
    url(r'^backend/api/v1/', include(rest_framework_urls)),
]
