from django.urls import path, include

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# router.register('country', views.CountryView)


urlpatterns = [
    path('', include(router.urls)),
    # path('UserLogin/', views.UserLoginApiView.as_view()),

]











