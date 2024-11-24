from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('main', views.main, name='mainn' ),
    path('cust/<int:pk>', views.cust, name='cust' ),
    path('proda/', views.prod, name='pro' ),
    path('', views.dahs, name='dashh' ),
    path('addOrder', views.add_order, name='addOO'),
    path('update/<int:pk>', views.update_order, name='upp'),
    path('del/<int:pk>', views.delete, name='dell'),
    path('addMore/<int:pk>', views.addMore, name='more'),
    path('Login', views.Login, name='login'),
    path('register', views.register, name='regist'),
    path('logout', views.logoutt, name='logout'),
    path('user', views.user, name='use'),
    path('edit', views.account, name='acc'),
    path('passReset/', auth_views.PasswordResetView.as_view(), name= 'password_change_done'),
    path('pass_sent/', auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    path('passCompleted/', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
    path('upload/', views.upload_file, name='upload_file'),
    path('show/', views.show, name='shows'),

]
# haoo    kennz

# https://chatgpt.com/c/ab47c6c9-7e13-4909-8277-c3505c1370b9
# https://github.com/django/django/blob/main/django/contrib/auth/urls.py