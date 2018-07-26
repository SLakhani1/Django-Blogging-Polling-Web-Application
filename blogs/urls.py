from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(template_name='blogs/index.html'), name='blogs'),
]