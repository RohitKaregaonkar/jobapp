from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:id>', views.job_details, name='job_details'),
    path('hello', views.hello),
]
