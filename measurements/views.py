from django.shortcuts import render
from .logic import logic_measurements
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def get_measurements(request):
    measurements = logic_measurements.get_all_measurements()
    measurement_list = serializers.serialize('json',measurements)
    return HttpResponse(measurement_list, content_type='application/json')


def get_measurent(request):
    measurement = logic_measurements.get_measurement(request)
    measurement_json = serializers.serialize('json',measurement)
    return HttpResponse(measurement_json, content_type='application/json')

def delete_measurement(request):
    measurement= logic_measurements.delete_measurement(request)
    measurement_json = serializers.serialize('json',measurement)
    return HttpResponse(measurement_json, content_type='application/json')

def change_measurement(request):
    measurement= logic_measurements.change_measurement(request)
    measurement_json = serializers.serialize('json',measurement)
    return HttpResponse(measurement_json, content_type='application/json')
