from django.urls import path,re_path,include
from .views import submit_info
from . import views

app_name='wanted'

urlpatterns = [
    re_path(r'^(?P<id>\d+)/submit_info$', submit_info),
]