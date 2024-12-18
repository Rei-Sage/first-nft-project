from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from workspace.forms import RegistrationForm, LoginForm

# Create your views here.

def creator(request):
    artist=Artist.objects.all()
    context={
        'artist':artist
    }
    return render(request,'creator.html',context)

def wallet(request):
    artist=Artist.objects.all()
    context={
        'artist':artist
    }
    return render(request,'wallet.html',context)

def ranking(request):
    artist=Artist.objects.all()
    paginator = Paginator(artist, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    context={
        'page_obj':page_obj,
    }
    return render(request,'ranking.html',context)


def market(request):
    nft=NFT.objects.all()
    context={
        'nft':nft
    }
    return render(request,'market.html',context)


def detail(request,id):
    product=NFT.objects.get(id=id)
    
    nft=NFT.objects.filter(creator=product.creator)
    
    context={
        'nft':nft,
        'product':product,
    }
    return render(request,'detail.html',context)

