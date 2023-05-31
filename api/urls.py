from django.urls import path
from api.views.user import *

urlpatterns = [
    # user
    path('user/', UserLoginRegisterView, name='user'),
    path('user/logout/', logout_view, name='logout'),
]
