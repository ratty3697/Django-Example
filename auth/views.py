from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
 
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):

	#Post request handling
	if request.method == 'POST':
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")

		#validating user
		user = authenticate(username = username , password = password)

		#if id/pw combination is wrong
		if user == None:
			status = 'wrong id/pw combination'

			#sending back Json Response
			return JsonResponse({'status':'ok','result':{'response':status}})
		else:
			status = 'logged in successfully'

			#generating token for user
			token = Token.objects.get_or_create(user=user)

			#sending back Json Response
			return JsonResponse({'status':'ok','result':{'response':status,'token':str(token[0])}})

	#other request handling except POST
	else:
		return JsonResponse({'status':'ok','result':{'response':'invalid request!!'}})


@csrf_exempt
def signup(request):

	#handling post request
	if request.method == 'POST':

		#creating user
		user = User.objects.create_user(request.POST.get("username",""), request.POST.get("email",""), request.POST.get("password",""))
		user.save()

		#sending back Json Response
		return JsonResponse({'status':'ok','result':{'response':'successfully created'}})

	#handling other requests
	else:
		#sending back Json Response
		return JsonResponse({'status':'ok','result':{'response':'invalid request!!'}})
