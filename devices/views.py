from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Device, TemperatureReading, HumidityReading
from .serializers import DeviceSerializer, TemperatureReadingSerializer, HumidityReadingSerializer
from django.shortcuts import render
from django.http import HttpResponseBadRequest

@api_view(['POST'])
def create_device(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_device(request, device_uid):
    try:
        device = Device.objects.get(uid=device_uid)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    device.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def retrieve_device(request, device_uid):
    try:
        device = Device.objects.get(uid=device_uid)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

@api_view(['GET'])
def list_devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_readings(request, device_uid, parameter):
    start_on = request.query_params.get('start_on')
    end_on = request.query_params.get('end_on')
    
    if not start_on or not end_on:
        return Response({"error": "start_on and end_on query parameters are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        device = Device.objects.get(uid=device_uid)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if parameter == 'temperature':
        readings = TemperatureReading.objects.filter(device=device, timestamp__range=[start_on, end_on])
        serializer = TemperatureReadingSerializer(readings, many=True)
    elif parameter == 'humidity':
        readings = HumidityReading.objects.filter(device=device, timestamp__range=[start_on, end_on])
        serializer = HumidityReadingSerializer(readings, many=True)
    else:
        return Response({"error": "Invalid parameter. Use 'temperature' or 'humidity'."}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data)


def device_graph(request):
    device_uid = request.GET.get('device_uid')
    
    if not device_uid:
        return HttpResponseBadRequest("Device UID is required")
    
    try:
        device = Device.objects.get(uid=device_uid)
    except Device.DoesNotExist:
        return HttpResponseBadRequest("Device not found")
    
    temperature_readings = TemperatureReading.objects.filter(device=device).order_by('timestamp')
    humidity_readings = HumidityReading.objects.filter(device=device).order_by('timestamp')
    
    context = {
        'device': device,
        'temperature_readings': temperature_readings,
        'humidity_readings': humidity_readings,
    }
    
    return render(request, 'devices/graph.html', context)
