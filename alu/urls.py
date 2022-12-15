from django.urls import path
from . import views
urlpatterns=[
    path('mainfun',views.mainfun,name="mainfun"),
    path('getdata',views.getData,name="getdata"),
    path('',views.mainForm,name="mainform"),
    
]