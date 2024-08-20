from django.urls import path
from . import views

urlpatterns = [
    path('api/devices/', views.list_devices, name='list_devices'),
    path('api/devices/', views.create_device, name='create_device'),
    path('api/devices/<str:device_uid>/', views.retrieve_device, name='retrieve_device'),
    path('api/devices/<str:device_uid>/', views.delete_device, name='delete_device'),
    path('api/devices/<str:device_uid>/readings/<str:parameter>/', views.list_readings, name='list_readings'),
    path('devices-graph/', views.device_graph, name='device_graph'),
]
