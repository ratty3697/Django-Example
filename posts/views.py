from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Posts
from rest_framework.authtoken.models import Token
from django.utils import timezone

@csrf_exempt
def addPosts(request):

	#Post request handling
	if request.method == 'POST':
		title = request.POST.get("title", "")
		data = request.POST.get("data", "")

		#getting token from header
		token = str(request.META.get('HTTP_AUTHORIZATION', '')).split(" ")[1]

		#getting token object to identify user
		token_object = Token.objects.get(key=token)

		#saving post to database
		q = Posts(title=title , data=data , pub_date=timezone.now() , user=str(token_object.user))
		q.save()
		
		return JsonResponse({'status':'ok','result':{'response':'post saved successfully'}})

	#other request handling except POST
	else:
		return JsonResponse({'status':'ok','result':{'response':'invalid request!!'}})

@csrf_exempt
def index(request):
	all_post = Posts.objects.order_by('pub_date')
	return render(request, "posts.html", {'data' : all_post})

