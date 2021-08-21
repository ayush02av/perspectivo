from django.shortcuts import render, redirect
from django.contrib import messages
from database.models import User, Work, Review, Vote

from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse
def Testing(request):
	return render(request, 'testing.html')

def AjaxTesting(request):
	if request.method == 'GET' and 'postid' in request.GET:
		postid = request.GET['postid'].upper()
		return HttpResponse(f'{postid}')
	else:
		return HttpResponse(f'Not a valid request')

def Index(request):
	if request.user.is_authenticated and "view-home" not in request.GET:
		return redirect(Feed)

	glimpses = Work.objects.all().order_by('-Rating')
	glimpses = glimpses if len(glimpses) <= 20 else glimpses[0:20]

	context = {
		'works':glimpses,
		'top_number':len(glimpses),
		'top_banner':True
	}

	# messages.success(request, 'Success!')
	# messages.warning(request, 'Warning!')
	# messages.error(request, 'Error!')
	# messages.info(request, 'Information!')

	return render(request, 'index.html', context)

def Feed(request):

	context = {
		'works':Work.objects.all(),
		'title':'Feed'
	}

	return render(request, 'feed.html', context)

def WorkDisplay(request, user, work):

	try:
		work = Work.objects.get(ByUser=User.objects.get(username=user), Title=work)
	except:
		return redirect(Index)

	context = {
		'work':work,
		'reviews':Review.objects.filter(ForWork=work),
		'title':work.Title,
		'upvotes':len(Vote.objects.filter(ForWork=work, Vote='UPVOTE')),
		'downvotes':len(Vote.objects.filter(ForWork=work, Vote='DOWNVOTE'))
	}

	return render(request, 'workdisplay.html', context)

def Account(request):

	if request.user.is_authenticated:
		return redirect(f'/profile/{request.user.username}')

	if request.method == "POST":
		
		if request.POST["submit"] == "Join":
			context = {
				'username':request.POST['username'],
				'name':request.POST['name'],
				'email':request.POST['email']
			}
			messages.info(request, 'Fill in these other details to complete your profile :)')
			return render(request, 'account.html', context)

		if request.POST["submit"] == "Sign Up":
			username = request.POST['username']
			name = request.POST['name']
			email = request.POST['email']
			number = request.POST['number']
			password = request.POST['password']
			passwordconfirm = request.POST['passwordconfirm']
			about = request.POST['about']

			first_name = name.split()[0]
			if len(name.split()) > 1:
				last_name = name.split(" ", 1)[1]
			else:
				last_name = ''

			context = {
				"username":username,
				"name":name,
				"email":email,
				"number":number,
				"about":about,
			}

			if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email=email)) == 0 and len(User.objects.filter(number=number)) == 0:
				if password == passwordconfirm:
					User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, number=number, about=about).save()
					messages.success(request, 'Account Created')
					login(request, User.objects.get(username=username))
					return redirect(f'/profile/{request.user.username}')
				else:
					messages.error(request, 'Passwords do not match')
			else:
				messages.error(request, 'Account Exists :/')

			return render(request, 'account.html', context)

		if request.POST['submit'] == "Log In":
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(username=username, password=password)
		
			if user != None:
				login(request, user)
				messages.success(request, "Successfully Logged In ;)")
				return redirect(f'/profile/{request.user.username}')
			else:
				messages.error(request, "Details didn't match :/")

	if request.user.is_authenticated:
		return redirect(f'/profile/{request.user.username}')
	else:
		return render(request, 'account.html')

def ProfileMiddle(request):
	if request.user.is_authenticated:
		return redirect(f'/profile/{request.user.username}')
	else:
		messages.warning(request, "You Need an Account First :)")
		return redirect(Account)

def Profile(request, user):

	if not request.user.is_authenticated:
		messages.warning(request, "You Need an Account First :)")
		return redirect(Account)

	try:
		user = User.objects.get(username=user)
		# user = request.user
	except:
		messages.error(request, 'No such user exists :(')
		return redirect(Account)
	else:
		context = {
			'user':user
		}

	return render(request, 'profile.html', context)

def Logout(request):
	logout(request)
	return redirect(Index)