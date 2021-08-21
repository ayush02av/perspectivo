from django.urls import path 

from .views import *

urlpatterns = [
	path('', Index),
	
	path('account/', Account),
	path('account/logout/', Logout),

	path('profile/', ProfileMiddle),
	path('profile/<str:user>/', Profile),

	path('feed/', Feed),
	path('<str:user>/<str:work>/', WorkDisplay),

	path('testing/', Testing),
	path('ajaxtesting/', AjaxTesting)
]