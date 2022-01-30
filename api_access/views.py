from django.shortcuts import render 
from django.http.response import HttpResponse,HttpResponseRedirect ,JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import messages
import requests 
import json




def handlelogin(request,id=None):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
         
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            user=request.user
            print("request.user:",request.user)
            # return render(request,"api_access/userhome.html")
            return HttpResponseRedirect("/dashboard/")

        else:
            return HttpResponse("<h4> invalid credentials !</h4>") 
    else:
        if id==None:
            return render(request,"plan_api/login.html")
        else :
            
            # mystore=Store.objects.get(id=id)
            return render(request,"plan_api/login.html",)

@login_required(login_url="/loginuser/")
def handlelogout(request,):
    logout(request)
    return HttpResponseRedirect("/")

 
def handleregister(request): 
    if request.method=="POST":
        user=request.user 
        Username=request.POST['username']
        First_name=request.POST['first_name']
        Last_name=request.POST['last_name']
        Email=request.POST['email']
        # Mobile_no=request.POST['Mobile_no']
        Password=request.POST['password']
        Cpassword = request.POST['cpassword']


        users_q=User.objects.all()  
        for u in users_q: 
            if Username ==u.username:
                messages.error(request,f"Username {Username} Already exists try another one !")
                return render(request,'plan_api/all_stores.html', )
       
        if len(Username)>10:
            messages.error(request,"Username must be less than 10 characters")
            return render(request,'plan_api/base.html', )


        if Password!=Cpassword:
            messages.error(request,"Confirmed password not match with passwod you entered ! ")
            return render(request,'plan_api/all_stores.html', )

        cr_user=User.objects.create_user(Username,Email,Password,is_staff=True)
        cr_user.first_name=First_name
        cr_user.last_name=Last_name
        cr_user.save() 
        Token.objects.create(user=cr_user)
        messages.success(request,f"New user {Username} created !")
        # return render(request,'stores/all_stores.html',{'stores':store_q,})
        return HttpResponseRedirect("/")
            
    else:
        
        return HttpResponseRedirect("login/") 


def home(request):
    return render(request,'plan_api/home.html', )

@login_required(login_url="/loginuser/")
def userhome(request):
    if request.method=="POST": 
        operator=request.POST['operator']  
        url="http://127.0.0.1:8000/plans/?service_provider="+operator
        r=requests.get(url)
        items=r.json()
        # item=dict(items[0])
        return render(request,"api_access/userhome.html",{"items":items})
    else :
        return render(request,"api_access/userhome.html" )
        
@login_required(login_url="/loginuser/")
def recharge(request):
    user=request.user 
    token=str(Token.objects.get(user=user))
    print(type(token))
    if request.method=="POST": 
        mobile_no=request.POST['mobile_no']  
        amount=request.POST['amount'] 
        print(mobile_no,amount,token) 
        url="http://127.0.0.1:8000/rechargeplan/?token="+token+"&mobile_no="+mobile_no+"&amount="+amount
        # url="http://127.0.0.1:8000/rechargeplan/"
        data={
            "token":token,
            "mobile_no":mobile_no,
            "amount":amount 
        }
        r=requests.post(url=url)
        items=r.text
        return HttpResponse(items)


 


 
 