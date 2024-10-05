from django.contrib import admin
from django.urls import path, include
from DjangoEcommerceApp import views
from django.conf.urls.static import static
from DjangoEcommerce import settings

urlpatterns = [
    path('admindashboard/', include("DjangoEcommerceApp.adminurls")),
    # Add this line for the root URL ('/')
    path('', views.demoPageTemplate, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
