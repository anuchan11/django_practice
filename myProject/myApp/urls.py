from django.conf.urls import url
from myApp import views

app_name = "myApp"
urlpatterns = [
    url(r'^$', views.index),
    url(r'^help/', views.help, name="help"),
    url(r'^table/', views.table),
    url(r'^fakeusers/', views.fakeusers),
    url(r'^form/', views.forms),
    url(r'^signup/', views.sign_up),
    url(r'^relative/', views.relative),
    url(r'^register/', views.register, name="register"),
    url(r'^user_login/$', views.user_login, name="user_login"),
]
