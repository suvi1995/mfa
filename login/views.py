from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
#from .models import ForgetPassword
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import uuid
import pyotp
from django.db.models.signals import post_save
from django.dispatch import receiver
#from .models import OtpToken
from datetime import datetime, timedelta
from django.utils import timezone
import random
from login.forms import SignUpForm
import qrcode
from io import BytesIO

SECRET_KEY = pyotp.random_base32()
# Create your views here.
def signup(request):
    if request.method == "POST":
        name=request.POST["username"]
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['Conform_Password']
        print(pass1)
        if pass1==pass2:
            
            return HttpResponseRedirect('/')
        else:
            messages.success(request, 'password mismatch')
    else:
        myform=SignUpForm()
        return render(request, "login.html", {'form': myform})
def login(request):
    if request.method=="POST":
        uname=request.POST['name']
        psw=request.POST['password']
        request.session['uname']=uname
        user=authenticate(username=uname, password=psw)
        if user is not None:
            return HttpResponseRedirect('mfa')                                                       
        else: 
            messages.error(request, 'your password is mismatch')
            return HttpResponseRedirect('/')
def home(request):
    return render(request, "home.html")
'''
def forgetpass_mail(request):
    if request.method=="POST":
        mail=request.POST['mail']
        token = str(uuid.uuid4())
        user= SignUpForm.objects.filter(email=mail).exists()
        if user:
            forget=ForgetPassword(email=mail, auth_token=token)
            forget.save()
            forgetpaa_mail(mail, token)
            messages.success(request, 'your password reset link set your register mail')
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'please enter valid email address')
            return HttpResponseRedirect('forgetpass_mail')
    return render(request,"forgetpass_mail.html")
    
def forgetpassword(request, token):
    profile_obj = ForgetPassword.objects.filter(auth_token=token).first()
    context={'user_id':profile_obj.id}
    if request.method=="POST":
        pass1=request.POST['password']
        pass2=request.POST['conformpassword']
        user_id=request.POST['user_id']
        if pass1==pass2:
            if User.objects.filter(id=user_id).first():
                print("rught")
            else:
                print("wrong")
    return render(request,"forget_password.html",context)
def forgetpaa_mail(email, token):
    subject = 'Your accounts need to be verified'
    message = f"""
    Hi
    paste the link to verify your account http://127.0.0.1:8000/forgetpassword/{token}
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
def mfa(request):
    if request.method=="POST":
        user_in=request.POST["auth"]
        if user_in=="qr":
            return HttpResponseRedirect('qr')
        else:
            request.session["otp_secret"] = SECRET_KEY
            return HttpResponseRedirect('mfa_otp')
    return render(request, 'mfa.html')
def qr(request):
    return render(request, 'qr.html')
def mfa_otp(request):
    if request.method == "POST":
        otp = request.POST["otp"]
        otp_secret = request.session.get("otp_secret")
        totp = pyotp.TOTP(otp_secret)
        otp_url = totp.provisioning_uri(name="user@example.com", issuer_name="MyApp")
        qr = qrcode.make(otp_url)
        buffer = BytesIO()
        qr.save(buffer)
        buffer.seek(0)
        #return HttpResponse(buffer, content_type="image/png")
        if totp.verify(otp):
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Invalid OTP")
    return render(request, 'otp.html')


    
    '''
