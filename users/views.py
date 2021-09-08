from django.shortcuts import render, redirect
from django.http.response import Http404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import Group
import requests
from django.contrib.auth import login, authenticate, logout


from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from decouple import config
from .models import User
from workdesk.models import Member


class UserBackend:
    """
    Backend to authenticate and return users.
    """
    def authenticate(self, request, user_name, full_name, current_year):
        """
        Authenticate users.

        1. Return user if present already.
        2. Create user and assign group if not present already.
        """
        if user_name:
            try:
                user = User.objects.get(username=user_name)
                return user
            except User.DoesNotExist:
                User.objects.create(username=user_name)
                user = User.objects.get(username=user_name)
                group = Group.objects.get(name='normaluser')
                user.groups.add(group)
                Member.objects.create(users=user, fullname=full_name, year=current_year)
        return user
  
    def get_user(self, user_id):
        """
        Get user and return user
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def login_redirect(request):
    """
    Function to redirect to channeli oAuth /oauth/authorise
    """
    return redirect(f"{config('SITE')}client_id={config('CLIENT_ID')}&redirect_uri={config('REDIRECT_URI')}")


def login_response(request):
    """
    Recieve access token and get user data.

    1. Post request with code to /open_auth/token/ and recieve access token
    2. Pass header to /open_auth/get_user_data/ and get user data
    3. Login if maintainer role present.
    """
    response = request.GET
    try:
        code = response["code"]
        post_data = {'client_id': f"{config('CLIENT_ID')}",
                     "client_secret": f"{config('CLIENT_SECRET')}",
                     "grant_type": "authorization_code",
                     "redirect_uri": f"{config('REDIRECT_URI')}",
                     "code": f"{code}"
                     }

        token_request = requests.post(f"{config('CODE_SITE')}", data=post_data)
        if token_request.status_code == 200:
            response = token_request.json()
        else:
            return HttpResponse(status=token_request.status_code) 

        access_token = response["access_token"]
        refresh_token = response["refresh_token"]
        data_request = requests.get(f"{config('TOKEN_SITE')}",
                                    headers={"Authorization": f"Bearer {access_token}"})
        if data_request.status_code == 200:
            data = data_request.json()
        else:
            return HttpResponse(status=token_request.status_code) 
        
        roles = data["person"]["roles"]
        roles_check = False
        for i in range(len(roles)):
            if roles[i]["role"] == 'Maintainer':
                roles_check = True
                
        if roles_check:
            user = authenticate(user_name=data["username"],
                                full_name=data["person"]["fullName"],
                                current_year=data["student"]["currentYear"])
            if user.is_active:
                user.save()
                login(request, user)
            else:
                return HttpResponseForbidden("You are not an active user")
        else:
            return HttpResponseForbidden("Site is accessible to maintainers only")
    except:
        raise Http404("Page not found")
    return HttpResponse('Logged into WorkDesk Successfully')


def logout_user(request):
    """
    Logout user.
    """
    if request.user.is_authenticated:
        logout(request)
        return redirect('/workdesk')
    else:
        return HttpResponseForbidden()
