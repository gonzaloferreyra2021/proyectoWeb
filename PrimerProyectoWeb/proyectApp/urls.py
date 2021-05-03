from django.urls import path
from proyectApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('contacto',views.contacto, name="contacto"),
    path('tienda',views.tienda, name="tienda"),
     
] 

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)