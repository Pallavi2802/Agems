from django import forms

class Login(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=40,widget=forms.PasswordInput)

class Signup(forms.Form):
    FirstName=forms.CharField(max_length=40)
    LastName=forms.CharField(max_length=40)
    Email = forms.EmailField(max_length=60)
    Username = forms.CharField(max_length=50,widget=forms.TextInput)
    Password = forms.CharField(max_length=40,widget=forms.PasswordInput)
    Confirmpassword = forms.CharField(max_length=50,widget=forms.PasswordInput)
    
class Forgot(forms.Form):
    Email=forms.EmailField()

class Verifyotp(forms.Form):
    Otp=forms.CharField(max_length=4,widget=forms.PasswordInput)

class Changepassword(forms.Form):
    New_pass=forms.CharField(max_length=40,widget=forms.PasswordInput)
    Conf_pass=forms.CharField(max_length=40,widget=forms.PasswordInput)