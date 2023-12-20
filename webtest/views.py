import random
from urllib.parse import urlencode
from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email

from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.csrf import ensure_csrf_cookie

from django.views.decorators.cache import cache_control
from Users.models import User
from django.urls import reverse

# Create your views here.

def HelloUser(request):
    return HttpResponse("This is the page of Hello User")

def Hello(request):
    return HttpResponse("This is the page of Hello Dipankar")


def index(request):
    return render(request, 'index.html')

def services(request):
    return HttpResponse("This is the page of services")

def contact(request):
    if request.method == "POST":
        try:
            name= request.POST["name"].upper()
            email= request.POST.get("email")
            phone= request.POST.get("phone")
            desc= request.POST.get("desc")
            try:
                validate_email(email)
            except validate_email.ValidationError:
                pass
            subject = 'SEMINAR GALLERY'
            message = f'Hi {name.split(" ")[0]},\nThank you for Conecting with us.\nYour Query ->  {desc} ,has been submitted and it is under process.\n\n\n\nRegards,\nSeminar gallery'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            try:
                send_mail( subject, message, email_from, recipient_list )
                communication_mail_status = "Yes"
                contact = Contact(name=name,email=email,phone=phone,desc=desc,communication_mail_status=communication_mail_status,date=datetime.today())
                contact.save()
                messages.success(request, 'Your query is registered and an acknowledge is sent to your email.')

            except:
                communication_mail_status = "No"
                messages.error(request, 'Your query unable to register please check your mail-id .')
            return redirect('contact')
        except:
            messages.error(request, 'Unable to submit your request. Thank you')
            return redirect('contact')
    else:   
        if request.user.is_authenticated and not request.user.is_superuser:
            print("hi")
            email = request.user.email
            fname = request.user.first_name
            lname = request.user.last_name

            context = {
                'email': email,
                'name':fname +" "+lname
            }
            return render(request, 'contact.html',context)
        else:
            messages.warning(request, 'You are not looged in to contact us please login,if you do not have any account then signup.')
            return redirect('login')
        

def calender(request):
    return render(request,'calender.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
        user_mail_id = request.POST["email"].lower()
        user_password = request.POST["password"]
        user = authenticate(email=user_mail_id, password=user_password)
        # print("Password:--->",user.password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Welcome")
            return redirect('user_interface')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')
    return render(request, 'login.html')


#for new users signup  ..... -------------------------------------------->

def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname'].upper()
        lastname = request.POST['lastname'].upper()
        user_email = request.POST['email'].lower()
        password = request.POST['password']
        confirmpassword = request.POST['confirm-password']
        try:
            if User.objects.get(email=user_email):
                messages.warning(request, 'Email alreday registered, try to SignIn.')     
        except:
            if (password == confirmpassword):    
                myuser = User.objects.create_user(user_email,password)
                myuser.first_name = firstname
                myuser.last_name = lastname
                try:
                    activation_key = random.randint(100000, 999999)
                    myuser.otp = activation_key
                   
                    #otp sent ------
                    subject = 'OTP verification(Seminar Gallery)'
                    htmlcontent = 'Hi <b>'+firstname.capitalize()+'</b>,<br>Welcome to seminar gallery.<div style="border: 2px solid black,background-color:black, color:white,border-radious:4px"><center><p></br>The OTP(one-time-password) is <b><h1>'+ str(activation_key)+'</b></h1></p></center></div>'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user_email]

                    sent = send_mail( subject, '', email_from, recipient_list,html_message=htmlcontent)
                    # sent = True
                    if sent :
                        myuser.save()
                        request.session['signup_email'] = user_email
                        messages.success(request, 'OTP(one-time-password) has been sent to your registered email address.')     
                        return redirect('signup_user_otp_validation')
                except:
                    messages.error(request, 'Unable to process your request try after some time .')
            else:
                messages.error(request, 'Password and confirm password did not match')     
        return redirect('signup')
    else:
       return render(request, 'signup.html')

def sending_mail_to_user(user_email,subject ,mesaage,htmlcontent):
    # email = request.session.get('signup_email')

   
    # lastname = user.last_name.upper().upper()
    # user_email = email
    if mesaage is not False:
        message = message
    else:
        message = " "
    
    if htmlcontent is not False:
        htmlcontent = htmlcontent
    else:
        htmlcontent = " "
    #otp sent ------
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    sent = send_mail( subject, message, email_from, recipient_list,html_message=htmlcontent)
    return sent 

def forgot_pass(request):
    if request.method == 'POST':
        user_mail_id = request.POST["email"].lower()
        user = User.objects.get(email=user_mail_id)

        if user is not None:
            request.session['signup_email'] = user_mail_id
            firstname = user.first_name.upper()
            activation_key = random.randint(100000, 999999)
            user.otp = activation_key
            user.save()
            subject = "Recover Password (Seminar Gallery)"
            html_content = 'Hi <b>'+firstname.capitalize()+'</b>,<br>Welcome to seminar gallery.<div style="border: 2px solid black,background-color:black, color:white,border-radious:4px"><center><p></br>The OTP(one-time-password) is <b><h1>'+ str(activation_key)+'</b></h1></p></center></div>'
            sent = sending_mail_to_user(user_mail_id,subject ,False,html_content)
            if sent :
                messages.success(request, 'OTP(one-time-password) has been sent to your registered email address.')     
                return redirect('otp_validation') 
    return render(request,'forgot-pass.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_interface(request):
    full_name = request.user.first_name.upper() + " " + request.user.last_name.upper()
    Is_staff = request.user.is_staff
    if Is_staff:
        context = {'full_name': full_name,'is_staff':"(admin)"}
    else:
        context = {'full_name': full_name}
    return render(request, 'user_interface.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth_logout(request)
    messages.info(request, 'Successfully logout.')     
    return redirect('login')


def signup_user_otp_validation(request):
    email = request.session.get('signup_email')
    print("Email_id:",email)
    if email :
        if request.method == 'POST':
            otp1 = request.POST.get('otp1')
            otp2 = request.POST.get('otp2')
            otp3 = request.POST.get('otp3')
            otp4 = request.POST.get('otp4')
            otp5 = request.POST.get('otp5')
            otp6 = request.POST.get('otp6')

            # concatenate the OTP values to get the full OTP
            otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6
            
            # validate the OTP and redirect accordingly
            user = User.objects.get(email = email)
           
            if user.otp == otp:
                user.is_active = True
                user.otp = None
                user.save()
                messages.success(request, 'OTP verified successfully. Your account is now active.')
                # mail service for registration
                subject = 'REGISTRATION AT SEMINAR GALLERY'
                message = f'Hi {user.first_name.capitalize()},\nWelcome to seminar gallery\nYour registraion details given below : \n\tName:{user.first_name+" "+user.last_name}\n\tEmail(username):{user.email}\n\tPassword:{user.password}\n\nNote: Please keep this for future references.\n\n\n\nRegards,\nSeminar gallery'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                sent = send_mail( subject, message, email_from, recipient_list )
                
                if sent :
                    messages.success(request, 'Credentials details have been sent to registered email.\n For login enter the credentials below.\n')     
                    del(request.session['signup_email'])
                else:
                    messages.error(request, 'Unable to sent details to the given email-id.')
                return redirect('login')
               
            else:
                messages.error(request,'Invalid OTP. Please try again.')
                return redirect('signup_user_otp_validation')        
        else:
            # render the OTP verification form
            return render(request, 'signup_user_otp_validation.html')

    else:
        messages.error(request,"Email address not found .")
        return redirect('signup')

   
def otp_validation(request):
    email = request.session.get('signup_email')
    # print("Email_id:",email)
    if email :
        if request.method == 'POST':
            otp1 = request.POST.get('otp1')
            otp2 = request.POST.get('otp2')
            otp3 = request.POST.get('otp3')
            otp4 = request.POST.get('otp4')
            otp5 = request.POST.get('otp5')
            otp6 = request.POST.get('otp6')

            # concatenate the OTP values to get the full OTP
            otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6
            
            # validate the OTP and redirect accordingly
            user = User.objects.get(email = email)
           
            if user.otp == otp:
                # messages.success(request,"OTP verified successfully")
                email = user.email.upper()
                messages.success(request,"Please enter your new password.")
                return redirect('reset_pass')
    return render(request,'otp_validation.html')

def reset_pass(request):
    email = request.session.get('signup_email')
    if request.method =="POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            try:
                user = User.objects.get(email = email)
                user.set_password(password1)
                user.save()
            except:
                messages.error(request,"Can't able to change the password rigt now, please try after some time .")
                return redirect("login")
            messages.success(request,'Your account password have been changed , try to login here .')
            return redirect('login')
        else:
            messages.error(request,"Password and confirm password does not match . try again")
            return redirect("reset_pass")
    else:
        
        content ={'email':email}
        return render(request,'reset_pass.html',content)

