from django.shortcuts import render
from django.http import JsonResponse
import requests


def home(request):
    return render(request, 'temperature/home.html')



def ajaxTemp(request):
    temp_sensor = '/sys/bus/w1/devices/28-0314640d89ff/w1_slave'

    try:
        tempStore = open(temp_sensor, 'r')	
        data = tempStore.read()
        tempStore.close()
        tempData = data.split("\n")[1].split(" ")[9]
        temperature = float(tempData[2:])
        temperature = round(temperature/1000,1)
    except:
        temperature = 0

    data = {
        'temperature':temperature,
    }

    return JsonResponse(data)


def gauge(request):
    return render(request, 'temperature/gauge.html')


def solar(request):
    return render(request, 'temperature/solar.html')



def ajaxSolar(request):

    URL = "http://192.168.1.50/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DeviceID=1&DataCollection=CommonInverterData"
    try:
        page = requests.get(URL)
        solarJson = page.json()
        power = solarJson["Body"]["Data"]["PAC"]["Value"]
    except:
        power = 0

    data = {'power': power}

    return JsonResponse(data)




##########################################################################################

def gaugeTest(request):
    return render(request, 'temperature/gaugecopy.html')
