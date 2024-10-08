from django.urls import path
from . import views

app_name='predictapp'

urlpatterns=[
    path("",views.predict_view,name='predict')
]