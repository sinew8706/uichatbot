from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

# Create your views here.

def index(request):
	return HttpResponse("<h1>hello~ home app!</h1>")


def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['버스', '지하철', '톡']

	})


@csrf_exempt
def message(request):
	message = ((request.body).decode('utf-8'))
	received_json_data = json.loads(message)
	return_str = received_json_data['content']


	return JsonResponse({
		'message' : {
		    'text' : return_str + '선택하셨습니다\n' + get_name(return_str)
		},
		'keyboard' : {
            'type':'text'
        },
	})


@csrf_exempt
def get_name(return_str):
    if return_str == '버스':
        return "------------\n" +  "버스번호를 입력하세요 \n"
    elif return_str == '지하철':
    	return "------------\n" +  "출발역을 입력하세요 \n"
    elif return_str == '톡':
    	return "------------\n" +  "말해보세요 \n"
    else :
    	return return_str + "이라고 쳤네~"