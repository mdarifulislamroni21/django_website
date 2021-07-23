from django.conf.urls import url
from django.urls import path
from daynamic import views
urlpatterns=[
    path('',views.registration_form,name='registration')
]
