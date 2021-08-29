from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.get_measurements, name='measurementsList'),
    path('get/', views.get_measurent, name='measurement'),
    path('change/',views.change_measurement, name='cahngeMeasurement'),
    path('delete/',views.delete_measurement, name='deleteMeasurement')
    ]