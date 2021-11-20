from User import views
from django.urls import path,include

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logoutUser,name='logout'),
    path('account-verify/<slug:token>',views.account_verify,name='account_verify')
]