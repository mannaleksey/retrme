from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views_static import *


@api_view(['GET'])
def load_to_db(request):
    mood = request.GET['mood']
    text = request.GET['text']
    person = request.GET['person']
    request_to_retrme(text, mood, person)
    response = {'nice': True}
    return Response(response)


@api_view(['GET'])
def get_from_db(request):
    person = request.GET['person']
    data = get_object_from_db(person)
    if data:
        response = {'success': True, 'text': data.response}
        delete_from_db(data)
        return Response(response)
    else:
        response = {'success': False}
        return Response(response)
