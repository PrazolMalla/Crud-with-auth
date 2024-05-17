from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password
import jwt
import datetime
from .models import CustomUser
import json

def create_payload(type,user,time):
    if (type == "access"):
        exp = datetime.datetime.now()+datetime.timedelta(minutes=time)
    else:
        exp = datetime.datetime.now()+datetime.timedelta(days=time)
    
    payload ={
            'type':type,
            'id':user.id,
            'exp':exp,
            'iat':datetime.datetime.now(),
            'user':user.email
        }
    return payload

def set_cookies(access_payload,refresh_payload):
    access_token = jwt.encode(access_payload,'secret',algorithm ='HS256')
    refresh_token = jwt.encode(refresh_payload,'secret',algorithm ='HS256')
    response = JsonResponse({'access token':access_token,'refresh token':refresh_token},status=204,safe=False)
    response.set_cookie(key='jwt',value=access_token,httponly=True)
    response.set_cookie(key='refresh_cookie',value=refresh_token)
    return response

def decode_token(token):
    decode_payload = jwt.decode(token,'secret',algorithms='HS256')
    return decode_payload

def login_required(func):
    def wrapper(request,*args, **kwargs):
        access_token=request.COOKIES.get('jwt')
        refresh_token = request.COOKIES.get('refresh_cookie')
        now = datetime.datetime.now()
        dt_now =int(now.timestamp())
        if not access_token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            access_token_payload=decode_token(access_token)
            
        except jwt.ExpiredSignatureError:
            return ("Error")
            
        wrapper.attrib = access_token_payload['id']


class UserDetail(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self,request):
        users = list(CustomUser.objects.values())
        return JsonResponse(users,status=200,safe=False)
    
    def post(self,request):
        data = json.loads(request.body)
        try:
            new_data = CustomUser(email = data["email"],password = make_password(data["password"]),address=data["address"],gender=data["gender"],isDeleted = data["isDeleted"])
            new_data.save()
            return JsonResponse({"created":data},safe=False)
        except:
            return JsonResponse({"error":"Not a Valid data"})
    
class UserInfo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self,request,id):
        user=list(CustomUser.objects.filter(pk=id).values())
        return JsonResponse(user,status=200,safe=False)
    
    def put(self, request, id):
        data = json.loads(request.body)
        try:
            new_user = CustomUser.objects.get(pk=id)
            data_key = list(data.keys())
            for key in data_key:
                if key == "email":
                    new_user.email = data[key]
                if key == "password":
                    new_user.password = make_password(data[key])
                if key == "phone":
                    new_user.phone = data[key]
                if key == "address":
                    new_user.address = data[key]
                if key == "gender":
                    new_user.gender = data[key]
                if key == "isDeleted":
                    new_user.isDeleted = data[key]
                new_user.save()
                return JsonResponse({"update":data},safe=False)
        except CustomUser.DoesNotExist:
            return JsonResponse({"error":"user doesn't exist"},safe=False)
        except:
            return JsonResponse({"error":"not a valid data "},safe=False)
    
    
    def delete(self, request, id):
        user = CustomUser.objects.get(pk=id)
        user.isDeleted = True
        user.save()
        return JsonResponse({"msg": "User deleted"}, status=204, safe=False)
    


class Login(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        password = data['password']  
        print(password)
        user = CustomUser.objects.filter(email=email).first() 
        if user is None:
            raise AuthenticationFailed('user not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Password not match')
        
        access_payload = create_payload("access",user,1)
        refresh_payload = create_payload("refresh",user,30)

        response = set_cookies(access_payload,refresh_payload)
        return response
        
    
class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        password = data['password']  
        user = CustomUser.objects.filter(email=email).first() 
        
        if user is None:
            raise AuthenticationFailed('user not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Password not match')
        

        access_token=request.COOKIES.get('jwt')
        refresh_token = request.COOKIES.get('refresh_cookie')
        now = datetime.datetime.now()
        dt_now =int(now.timestamp())
        print(dt_now)
        if not access_token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            access_token_payload=jwt.decode(access_token,'secret',algorithms='HS256')
            if email != access_token_payload['user']:
                raise AuthenticationFailed('Unauthenticated')
            
        except jwt.ExpiredSignatureError:
            refresh_token_payload = jwt.decode(refresh_token,'secret',algorithms='HS256')
            if dt_now < refresh_token_payload['exp']:
                new_access_payload = create_payload("access",user,1)
                new_access_token = jwt.encode(new_access_payload,'secret',algorithm ='HS256')
                response = JsonResponse({'access token':new_access_token},status=204,safe=False)
                response.set_cookie(key='jwt',value=new_access_token,httponly=True)
                return response
            else:
                raise AuthenticationFailed('fdaj')
            # raise AuthenticationFailed('Expired')

        return JsonResponse(access_token_payload,safe=False)