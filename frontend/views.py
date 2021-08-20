from django.shortcuts import render, redirect
from database.models import User, Work

def Index(request):

	glimpses = Work.objects.all() if len(Work.objects.all()) <= 20 else Work.objects.all()[0:20]

	context = {
		'works':glimpses,
		'top_number':len(glimpses),
		'top_banner':True
	}

	return render(request, 'index.html', context)

def Feed(request):
	return render(request, 'feed.html', {'works':Work.objects.all()})

def WorkDisplay(request, user, work):

	try:
		work = Work.objects.get(ByUser=User.objects.get(username=user), Title=work)
	except:
		return redirect(Index)

	context = {
		'user':user,
		'work':work
	}

	return render(request, 'workdisplay.html', context)