from Login_App import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout')
]
