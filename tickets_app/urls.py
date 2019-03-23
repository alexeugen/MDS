from django.urls import path
from . import views

urlpatterns = [
    # home page-> calls home function
    path('', views.home, name='tickets-home'),
    #about page
    path('about/', views.about, name='tickets-about'),
    path('register/', views.about, name='tickets-register'),
    path('login/', views.about, name='tickets-login'),
]
