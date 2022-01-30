  
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotAllowed,JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view 
from .serializers import PlanSerializer 
from .models import Plan, Service_provider


@api_view([ 'GET', ])
def plans(request):
    if request.method =='GET':
        data=request.query_params
        if 'service_provider' in data :
            service_provider=data['service_provider']
            service_provider_q=Service_provider.objects.filter(name=service_provider)
            print(service_provider_q)
            plan_q=Plan.objects.filter(service_provider__in=service_provider_q)
        else:
            plan_q=Plan.objects.all()
    serializer = PlanSerializer(plan_q,many=True)
    return JsonResponse(serializer.data,safe=False) 


@api_view([ 'POST', ])
def recharge_plan(request):
    if request.method =='POST':
        data=request.query_params
        token=data['token']
        mobile_no=data['mobile_no']
        price=data['amount'] 
        check_token=Token.objects.filter(key=token)
        if check_token :
            return  Response("Recharge done")
        
        else :
            return  Response("Invalid Token")

    


