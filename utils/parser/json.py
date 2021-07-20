
import io
import json
from json.encoder import JSONEncoder
from django.http.response import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

def json_to_data(json_body: bytes):
    stream = io.BytesIO(json_body)
    return JSONParser().parse(stream)

def response_success(message):
    response = {}
    response['version'] = '0.0.1'
    response['message'] = message
    return HttpResponse(JSONRenderer().render(response), content_type='application/json')

def response_data(data: object):
    response = {}
    response['version'] = '0.0.1'
    response['data'] = data
    return HttpResponse(JSONRenderer().render(response), content_type='application/json')

def response_items(items: list):
    response = {}
    response['version'] = '0.0.1'
    response['items'] = items
    return HttpResponse(JSONRenderer().render(response), content_type='application/json')