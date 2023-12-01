from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django.conf import settings
import googlemaps

from .models import User, GymDetail





# Create your views here.
def index(request):

    #criar variavel para puxar todas as academias 
    allgym = GymDetail.objects.all()

    #renderizar
    return render(request, "project/index.html", {
        'allgym':allgym
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "project/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "project/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "project/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "project/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "project/register.html")
    
#criar funcao detail
def detail(request,gymid):

#criar variavel para puxar a tabela Gymdetail

    gymdetail = GymDetail.objects.get(id=gymid)

#puxar todas as infos de uma acad especifica
    return render(request, "project/detail.html", {
        'gymdetail':gymdetail
    })

#renderiza e envia para o html da "Gymdetail"

#criar html
#mostrar todas as infos de uma academia selecionada pelo usuario

def category(request):
    if request.method == "POST":
        category_name = request.POST["category"]
        filter_args = {f'{category_name.lower()}__exact': True}  # or use '__iexact' for case-insensitive
        allgym = GymDetail.objects.filter(**filter_args)
        return render(request, "project/index.html", {
            "allgym": allgym
        })

def address(request):
    if request.method == "GET":
        return render(request, "project/findagym.html")
    else:
        street = request.POST["street"] 
        city = request.POST["city"] 
        neighborhood = request.POST["neighborhood"] 
        state = request.POST["state"] 
        
        endereco = street+ " " +city + " " + neighborhood + " " + state

        nearby_location = GymDetail.objects.all().values_list('endereco', flat=True)  # Fetching all addresses


        return render(request, "project/google.html", {
                "address": endereco,
                "nearby_gyms": nearby_location
            })
