from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import AccessRecord, Topic, WebPage, FakeUsers, SignUp
from myApp.forms import BasicForm, SignupForm, UsersForm, UserPortfolioInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def index(request):
    dict = {"variable_from_views": "Okay this is also wierd, it came from sub dir"}
    return render(request, "myApp/index.html", context=dict)


def help(request):
    dict = {"help":"HELP PAGE"}
    return render(request, "myApp/help.html", context=dict)


def table(request):
    acc_rec = AccessRecord.objects.order_by('date')
    dict = {"access_records": acc_rec}
    return render(request, "myApp/table.html", context=dict)


def fakeusers(request):
    users = FakeUsers.objects.order_by("fname")
    dict = {"users": users }
    return render(request, "myApp/users.html", context=dict)


def forms(request):
    form = BasicForm()

    if request.method == "POST": #checking if form is submitted
        form = BasicForm(request.POST)

        if form.is_valid(): #defualt function to check validity
            print("Valid data passed!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: "+ form.cleaned_data['email'])
    dict = {"form":form}
    return render(request, "myApp/forms.html", dict)


def sign_up(request):
    signup = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if  form.is_valid():
            form.save(commit=True)  #just saves it directly to model
            #user = SignUp(name=form.cleaned_data['name'], email=form.cleaned_data['email']) #we can use this too to save to model SignUp
            #user.save()
            return index(request) #upon hitting submit, takes back to homepage index
    return render(request, "myApp/signup.html", {"signup": signup})



def relative(request):
    return render(request, "myApp/relative.html")



@login_required
def user_logout(request):
    logout(request)
    return HttpResponse("Thank you, see you back soon!")

def register(request):
    registered = False

    if request.method == "POST":
        usersform = UsersForm(data=request.POST)
        userprofile = UserPortfolioInfoForm(data = request.POST)
        if usersform.is_valid() and userprofile.is_valid():
            user = usersform.save()
            user.set_password(user.password)
            user.save()

            profile = userprofile.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(usersform.errors, userprofile.errors)
    else:
        usersform = UsersForm()
        userprofile = UserPortfolioInfoForm()
    return render(request, 'myApp/register.html', {'user_form':usersform, 'user_portfolioform': userprofile, 'registered': registered})





def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!!")
        else:
            print(f"{username} logged in with {password}, invalid.")
            return HttpResponse("INVALID CREDENTIALS!")
    else:
        return render(request, 'myApp/user_login.html', {})
