from django.shortcuts import render
from . import forms

#for login logout:-
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#note: dont call a view to something which you import


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered=False

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        profile_form=forms.UserProfileInfoForm(request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            #hashing the password
            user.save()
            #save the changes

            profile= profile_form.save(commit=False)
            profile.user = user
            #this sets up the one to one relationship

            #to check if there is in an image
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered= True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form= forms.UserForm()
        profile_form= forms.UserProfileInfoForm()

    return render(request,'basic_app/register.html',
    {"user_form":user_form,'profile_form':profile_form,'registered':registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



@login_required
def special(request):
    logout(request)
    return HttpResponse("Congragulations! U have logged in !")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #getting what the user has inputted via the name of the corresponding html tags

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                #redirecting to home page
                return HttpResponseRedirect(reverse('special'))

            else:
                return HttpResponse("Account not acitve")

        else:
            print("Someone tried to login and failed!")
            print("Username :{} and password {}".format(username,password))
            return HttpResponse('invalid login details!')

    else:
        return render(request,'basic_app/login.html',{})
