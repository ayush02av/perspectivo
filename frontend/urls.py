from django.urls import path 

from .views import *

urlpatterns = [
	path('', Index),
	path('feed/', Feed),
	path('<str:user>/<str:work>/', WorkDisplay)
]