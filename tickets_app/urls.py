from django.urls import path
from . import views

urlpatterns = [
    # home page-> calls home function
    path('', views.home, name='tickets-home'),
    #about page
    path('about/', views.about, name='tickets-about'),
    #login page
    path('login/', views.login, name='tickets-login'),
    #register page
    path('register/', views.register, name='tickets-register'),
]
