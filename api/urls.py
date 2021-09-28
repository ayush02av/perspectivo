from django.urls import path

from . import views

urlpatterns = [
	path('works/', views.Work_API),
	path('glimpses/', views.Glimpses),
]