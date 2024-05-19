from django.urls import path
from myresuma import views

urlpatterns = [
    path('', views.my_view, name='my-view'),
]

