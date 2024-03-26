from django.urls import path
from accounts.views import *

urlpatterns = [
    path('',loginpage,name='loginpage'),
    path('line/login/callback/', line_login_callback, name='line_login_callback'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]