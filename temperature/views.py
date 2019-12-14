from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, 'temperature/home.html')



def ajaxTemp(request):
    temp_sensor = '/sys/bus/w1/devices/28-0314640d89ff/w1_slave'

    tempStore = open(temp_sensor, 'r')	
    data = tempStore.read()
    tempStore.close()
    tempData = data.split("\n")[1].split(" ")[9]
    temperature = float(tempData[2:])
    temperature = round(temperature/1000,1)

    return JsonResponse(temperature)
