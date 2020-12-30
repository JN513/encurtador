from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from .models import Url

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def create_url(request):
    url = request.POST['url']
    url = Url(full_url=url)
    url.save()

    data = {
        'full_url':url.full_url,
        'hash':url.short_url,
    }

    return render(request, 'pages/created.html', data)

def redirect(request, hash):
    url = get_object_or_404(Url, short_url=hash)
    url.clicked()

    return HttpResponseRedirect(url.full_url)

def url(request):
    url = request.GET['hash']
    url = get_object_or_404(Url, short_url=url)

    data = {
        'full_url':url.full_url,
        'hash':url.short_url,
        'clicks':url.clicks,
        'created':url.created,
    }

    return render(request, 'pages/url.html', data)