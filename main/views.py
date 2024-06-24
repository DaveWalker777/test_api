from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ad
from .serializers import AdSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm


class AdDetail(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


def ads_list(request):
    ads = Ad.objects.all().order_by('id')[:10]
    return render(request, 'ads_list.html', {'ads': ads})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you were logged in")
            return redirect('ads-list')
        else:
            messages.error(request, "Username or password are invalid")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "you were logged out")
    return redirect('ads-list')


def register_user(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'New profile was created for ' + user)
            return redirect('login')

    return render(request, 'register_user.html', {
        'form': form,
    })


@api_view(['GET'])
def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    serializer = AdSerializer(ad)
    return Response(serializer.data)


@api_view(['GET'])
def ad_list(request):
    ads = Ad.objects.all()
    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)