from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name='home'),
    path('contact/',views.contact ,name='contact'),
    path('about/',views.about ,name='about'),
    path('user/',views.user,name="user"),
    path('buy/',views.buyproduct,name="buy"),
    path('user_details/<int:regid>/',views.user_def,name="user_details"),
    path('edid_user/<int:priid>/',views.edid_user,name="edid_user"),
    path('edid_product/<int:product_id>/',views.edid_product,name="edid_product"),
    path('delete_product/<int:product_pk>/',views.delete_product,name="delete_product"),
    path('delete_user/<int:userid>/',views.delete_user,name="delete_user"),
    path('registration/',include('daynamic.urls'),name="registration")

]
