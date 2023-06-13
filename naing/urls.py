from django.urls import path
from naing import views
urlpatterns =[
    path ('', views.index, name='indexpage')
]