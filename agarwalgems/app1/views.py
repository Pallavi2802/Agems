from django.shortcuts import render
from .forms import Login,Signup,Forgot,Verifyotp,Changepassword
from django.views import View
from .models import AddUser
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.
to_email=""
otp=""
def index(request):
    return render(request,"try.html")

def tryout(request):
    return render(request,"trylogout.html")


def bluesapphire(request):
    if request.session.get('email'):
        data=" already login ..."
        return render(request,"blue.html")
    else:
        form=Login()
        return render(request,"login.html")
    
def emerald(request):
    if request.session.get('email'):
        data=" already login ..."
        return render(request,"emerald.html")
    else:
        form=Login()
        return render(request,"login.html")

def opal(request):
    if request.session.get('email'):
        data=" already login ..."
        return render(request,"opal.html")
    else:
        form=Login()
        return render(request,"login.html")

def ruby(request):
    if request.session.get('email'):
        data=" already login ..."
        return render(request,"ruby.html")
    else:
        form=Login()
        return render(request,"login.html")  

def account(request):
    return render(request,"account.html")

def login(request):
    if request.session.get('email'):
        data="Already logged in ..."
        return render(request,"try.html")
    else:
        form=Login()
        return render(request,"login.html")

def login1(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            #print(form)
            email = form.cleaned_data['Email']
            try:
                u = AddUser.objects.get(Email=email)
            except AddUser.DoesNotExist as e:
                    error="no such user ... signup to login"
                    form=signup()
                    return render(request,"signup.html")
            else:
                password = form.cleaned_data['Password']
                p=u.Password
                if password == p:
                    request.session['email'] = email
                    request.session['password'] = p
                    return render(request,"trylogout.html")
                    #return HttpResponse("<h1 style='color:red'>Welcome user {} with password {}".format(email,password))
                else:
                    error="Password does not match"
                    form=Login()
                    return render(request,"login.html",{'error':error})
        else:
            error = "Form is not valid...Try again"
            return render(request,"login.html",{'error':error})
    else:
        error = "Incorrect method used"
        return render(request,"login.html",{'error':error})

def buyinguide(request):
    if request.session.get('email'):
        user = AddUser.objects.get(Email=request.session.get('email'))
        u=user.Username
        data=" already login ..."
        return render(request,"buyinguide.html",{'u':u})
    else:
        form=Login()
        return render(request,"login.html")
    
def more(request):
    if request.session.get('email'):
        user = AddUser.objects.get(Email=request.session.get('email'))
        u=user.Username
        data=" already login ..."
        return render(request,"more.html",{'u':u})
    else:
        form=Login()
        return render(request,"login.html")
   
def signup(request):
    form = Signup()
    return render(request,"signup.html")

class Signedup(View):
    def get(self,request):
        form = Signup()
        error = "Your method is incorrect..."
        return render(request,"signup.html",{'error':error})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data['Email']
            try:
                AddUser.objects.get(Email=email)
            except AddUser.DoesNotExist as e:
                pass1 = form.cleaned_data['Password']
                pass2 = form.cleaned_data['Confirmpassword']
                if pass1 == pass2:
                    dict = {
                     'FirstName':form.cleaned_data['FirstName'],
                     'LastName':form.cleaned_data['LastName'],
                     'Username' : form.cleaned_data['Username'],
                     'Email' : form.cleaned_data['Email'],
                     'Password' : form.cleaned_data['Password'],
                      # 'Profile' : form.cleaned_data['Profile'],
                        }
                    new_user = AddUser.objects.create(**dict)
                    new_user.save()
                    return render(request,"1page.html")
            else:
                error = "Password does not match...Try again"
                form = Signup()
                return render(request,"signup.html",{'error':error})
        else:
            error = "Your form is invalid...try again"
            form = Signup()
            return render(request,"signup.html",{'error':error})


def logout(request):
    del request.session['email']
    del request.session['password']
    return render(request,"try.html")

def forgot(request):
    form = Forgot()
    error="plx try again"
    return render(request,"forgot.html",{'error':error})


def send_otp(request):
    form=Forgot(request.POST)
    if form.is_valid():
        global to_email
        global otp
        to_email=form.cleaned_data['Email']
        try:

            user=AddUser.objects.get(Email=to_email)
            from_email=settings.EMAIL_HOST_USER
            subject="Mail for otp "
            otp = str(random.randint(0000,9999))
            message = "Change password using this otp" + otp
            send_mail(subject,message,from_email,(to_email,),auth_password=settings.EMAIL_HOST_PASSWORD)
            form2=Verifyotp()
            return render(request,"verify_otp.html",{'form2':form2,'Email':to_email})
        
        except AddUser.DoesNotExist as e:
            error="Email is not registered"
            return render(request,"forgot.html",{'error':error})

def verify_otp(request):
    form=Verifyotp(request.POST)
    global to_email
    global otp
    if form.is_valid():
        Otp=form.cleaned_data['Otp']
        if Otp == otp:
            form2=Changepassword()
            return render(request,"change_pass.html",{'form':form2,'Email':to_email})
        else:
            error="Otp does not match"
            return render(request,"verify_otp.html",{'error':error})
    else:
        error="Form is invalid"
        return render(request,"verify_otp.html",{'error':error})

def change_pass(request):
    form=Changepassword()
    global to_email
    return render(request,"change_pass.html",{'form':form,'Email':to_email})

def verify_pass(request):
    global to_email
    form=Changepassword(request.POST)
    if form.is_valid():
        New_pass=form.cleaned_data['New_pass']
        Conf_pass=form.cleaned_data['Conf_pass']
        if New_pass==Conf_pass:
            user=AddUser.objects.get(Email=to_email)
            user.Password=New_pass
            user.save()
            error="Password Changed"
            return render(request,"login.html",{'error':error})
        else:
            error="Password does not match"
            return render(request,"change_pass.html",{'error':error})
    else:
        error="Form invalid"
        return render(request,"change_pass.html",{'error':error})


