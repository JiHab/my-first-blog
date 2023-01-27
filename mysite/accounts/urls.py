from django.conf.urls import url
from . import views
from django.contrib.auth.views import auth_login, auth_logout, logout_then_login, LoginView, LogoutView
from django.contrib.auth import login, logout

urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
]