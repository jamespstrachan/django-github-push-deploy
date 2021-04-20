from django.urls import path
from . import views

app_name = 'django_github_push_deploy'
urlpatterns = [
    path('deploy', views.deploy, name='deploy'),
]
