from django.contrib.sites import requests
from django.shortcuts import render
from django.http import JsonResponse
from personal.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import requests


@csrf_exempt
def apiCourse(request):
    if (request.method == "GET"):
        # Serialize the data into json
        data = serializers.serialize("json", Course.objects.all())
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

    if (request.method == "POST"):
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # filter data
        if not body:
                data = '{"message": "data is not json type!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
        else:
            created = Course.objects.create(
                course_name=body['course_name']
            )
            data = '{"message": "data successfully created!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

    if (request.method == "DELETE"):
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        else:
            course_id = body.get('course_id')
            if course_id:
                course = Course.objects.get(id=course_id).delete()
                data = '{"message": "data successfully deleted!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
            else:
                data = '{"message": "data is not json type!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)

    if (request.method == "PUT"):
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        else:
            course_id = body.get('course_id')
            if course_id:
                course = Course.objects.get(id=course_id)
                course.course_name = body.get('course_name')
                course.save()
                data = '{"message": "data successfully updated!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
            else:
                data = '{"message": "data is not json type!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)

@csrf_exempt
def consumeApiGet(request):
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

        api_url = body.get('api_url')
        if api_url:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return render(request, "personal/api-get.html", {'data': data})
            else:
                data = '{"message": "failed to fetch data from the API!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
        else:
            data = '{"message": "api_url is missing!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

    if request.method == "PUT":
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

        api_url = body.get('api_url')
        update_data = body.get('update_data')
        if api_url and update_data:
            response = requests.put(api_url, json=update_data)
            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data, safe=False)
            else:
                data = '{"message": "failed to update data at the API!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
        else:
            data = '{"message": "api_url or update_data is missing!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

    # Default GET request handling
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    return render(request, "personal/api-get.html", {'data': data})