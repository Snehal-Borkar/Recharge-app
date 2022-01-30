from rest_framework import serializers
from  .models import Plan,Service_provider
class PlanSerializer(serializers.ModelSerializer): 
    service_provider = serializers.CharField(source='service_provider.name')
    price =serializers.FloatField()
    talktime=serializers.CharField()
    data=serializers.CharField()
    validity=serializers.CharField()
    sms=serializers.CharField()
    other_details=serializers.CharField()
    class Meta:
        model = Plan
        fields=['id','service_provider','price','talktime','data','validity','sms','other_details'] 
