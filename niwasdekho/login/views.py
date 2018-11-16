from django.shortcuts import render
from login.forms import UserInfoForm,UserProfileForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from login.models import UserProfileInfo
from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    REGISTERED = False

    if request.method=='POST':

        user_info = UserInfoForm(request.POST)

        if user_info.is_valid() :

            user = user_info.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('login/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = user_info.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

            REGISTERED=True

        else:
            print(user_info.errors)
    else:

        user_info = UserInfoForm()

    return render(request,'login/register.html',{'user_info':user_info,'registered':REGISTERED})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('register/register/')
    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request):

    if request.method=='POST':

        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(request , username = username , password = passw)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("credentials are wrong")

    else:
        return render(request,'login/user_login.html',{})


def forget_pass(request):

    if request.method == 'POST':
        email_id = request.POST['email']
        try:
            user = User.objects.get(email=email_id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None :
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('login/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            return HttpResponse('email is sended to u ')

        else:
            return HttpResponse('you are not registered')

    else:
        return render(request,'login/forgot.html',{})



def user_profile(request):

    if request.user.is_authenticated:
        id = request.user.id
        name_user = request.user.first_name
        path_img = UserProfileInfo.objects.get(user_id=id).profile_pic.url



        dict = {'img_path':path_img,'name':name_user}
        return render(request,'login/profile.html',dict)
    else:
        return HttpResponse("you are not logged in")
