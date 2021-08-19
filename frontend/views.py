from django.shortcuts import render
from database.models import Work

def Index(request):

	glimpses = Work.objects.all() if len(Work.objects.all()) <= 20 else Work.objects.all()[0:20]

	context = {
		'works':glimpses,
		'top_number':len(glimpses),
		'top_banner':True
	}

	return render(request, 'index.html', context)