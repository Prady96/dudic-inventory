from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .admin import SendUserEmails

router = DefaultRouter()




urlpatterns = [
    path('', include(router.urls)),
    url(r'^email-users/$',view=SendUserEmails.as_view(),name='email'),

]











