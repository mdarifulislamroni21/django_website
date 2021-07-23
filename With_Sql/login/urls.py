from django.conf.urls import url
from django.urls import path
from login import views
urlpatterns=[
    path('',views.login,name="login")
]
