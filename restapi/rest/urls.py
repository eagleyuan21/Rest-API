from django.contrib import admin
from django.urls import path
from arbitrary import views

urlpatterns = [
    path('admin/', admin.site.urls), # admin endpoint 
    path('api/objects', views.arblist.as_view()), # general api/objects endpoint
    path('api/objects/<str:uid>', views.arbdetails.as_view()) # uid endpoint
]
