# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint
import requests

from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.urls import url
from django.db import connection
cursor = connection.cursor()

@login_required
def default(request):
    return render(request,'userinfo/index.html')

@login_required
def dashboard(request):
    return render(request,'userinfo/dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'userinfo/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        # profile_form = UserInfoForm(data= request.POST)

        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user
            #
            # profile.save()
            #
            # print profile.Phone_number
            current_site = get_current_site(request)
            message = render_to_string('userinfo/acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'userinfo/acc_active_sent.html')
            # registered = True
        else: print user_form.errors
            # print user_form.errors, profile_form.errors
    else: user_form = UserForm()
        # profile_form = UserInfoForm()

    return render(request,'userinfo/registration.html',
                    {'user_form': user_form,
                     # 'profile_form': profile_form,
                     'registered': registered
                     })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active: login(request, user);return redirect('info/dashboard/')
            else: return HttpResponse("Account is not Active!")
        else:
            print "Someone Tried to login and failed!"
            print "Username : {} and password : {}".format(username, password)
            return HttpResponse("Invalid Login Credentials Passed!")
    else: return render(request, 'userinfo/login.html', {})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        request.session['uid'] = uid
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): user = None
    if user is not None and account_activation_token.check_token(user, token):
        # user.is_active = True
        # user.save()
        # login(request, user)
        return redirect('info/contact/')
    else:
        return HttpResponse('Activation link is invalid!')

def contact(request):
    if request.method == 'POST':
        receivernum = request.POST.get('contact')
        request.session['number'] = receivernum

        verification_code = randint(100000,999999)
        request.session['otp_verify'] = verification_code


        url = 'https://2factor.in/API/V1/5a-a895-0200cd936042-7a93d9-bbb5-11e8/SMS/'+str(receivernum)+'/'+str(verification_code)
        req = requests.get(url)
        if req.status_code == 200: return redirect('info/verify/')
        else: return HttpResponse("Error Occured During Sms Sending........")
    else: return render(request, 'userinfo/contact.html', {})

def contact_verify(request):
    verification_code = request.session['otp_verify']
    if request.method == 'POST':
        uid = request.session['uid']
        user = User.objects.get(pk = uid)
        OTP = request.POST.get('OTP')
        if int(verification_code) == int(OTP):
            receivernum = request.session['number']
            # cursor.execute("""INSERT INTO userinfo_userinfo(Phone_number) VALUES('{}')""".format(receivernum))
            user.is_active = True
            user.save()
            login(request, user)
            # return HttpResponse("Your Mobile Number Has Been Successfully Updated")
            return redirect('info/user_login/')
        else:
            return HttpResponse("Invalid OTP ")
    else:
        return render(request,'userinfo/contact_confirm.html')

def user_resetpassword(request):
    return render(request,'userinfo/resetpassword.html')
