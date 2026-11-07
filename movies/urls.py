from django.urls import path
from movies import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]