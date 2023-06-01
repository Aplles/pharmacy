from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from models_app.models import Cart, Product, Category
from models_app.models.user.models import User


class UserLoginRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vhod.html')


class UserRegisterRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registr.html')


class UserLoginRegisterView(View):

    def get(self, request, *args, **kwargs):
        user = authenticate(request, username=request.GET['username'], password=request.GET['password'])
        if user:
            login(request, user)
            products = Product.objects.all()
            if len(products) > 5:
                products = products[:5]
            return render(request, 'index.html', context={
                "popular_products": products,
                "categories": Category.objects.all()
            })
        return render(request, 'vhod.html', context={'error': 'Неверный логин или пароль'})

    def post(self, request, *args, **kwargs):
        if request.POST["password"] != request.POST["psw-repeat"]:
            return render(request, 'registr.html', context={'error': 'Пароли не совпадают'})
        try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                       email=request.POST['email'])
            cart = Cart.objects.create(
                user=user
            )
            return render(request, 'vhod.html')
        except Exception as e:
            return render(request, 'registr.html', context={'error': 'Пользователь с таким именем уже существует'})


class UserUpdateInfoView(View):

    def post(self, request, *args, **kwargs):
        user = request.user
        if request.POST['username']:
            try:
                user.username = request.POST['username']
            except Exception:
                return render(request, 'user/account.html',
                              context={'error': 'Пользователь с таким именем уже существует'})
        if request.POST['email']:
            user.email = request.POST['email']
        user.save()
        return render(request, 'user/settings.html')


class UserUpdatePasswordView(View):

    def post(self, request, *args, **kwargs):
        user = request.user
        if request.POST['new_pass']:
            if user.check_password(request.POST['pass']):
                user.set_password(request.POST['new_pass'])
        user.save()
        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('index')
