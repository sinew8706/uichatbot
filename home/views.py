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
	print(return_str)


	return JsonResponse({
		'message' : {
		    'text' : '입력을 확인합니다\n' + return_str + '\n' + get_name(return_str)
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


@csrf_exempt
def webhook(request):
	message2 = ((request.body).decode('utf-8'))
	print(message2)
	received_json_data = json.loads(message2)
	bus_stop = received_json_data['result']['parameters']['bus_stop']
	bus_number = received_json_data['result']['parameters']['bus_number']
	speech = received_json_data['result']['fulfillment']['speech']
	print(bus_stop)
	print(bus_number)
	print(speech)

	pass