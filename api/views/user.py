from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import View
from models_app.models.user.models import User


class UserLoginRegisterView(View):

    def get(self, request, *args, **kwargs):
        user = authenticate(username=request.GET['username'], password=request.GET['password'])
        if user:
            login(request, user)
            return render(request, 'index.html')
        return render(request, 'login.html', context={'error': 'Неверный логин или пароль'})

    def post(self, request, *args, **kwargs):
        try:
            User.objects.create(username=request.POST['username'], password=request.POST['password'],
                                email=request.POST['email'])
            return render(request, 'login.html')
        except Exception:
            return render(request, 'register.html', context={'error': 'Пользователь с таким именем уже существует'})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')
