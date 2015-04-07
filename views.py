from django.http import JsonResponse
import datetime

def current_datetime(request):
    time = datetime.datetime.now()
    text = "It is now %s." % time
    json = {'text': text}
    return JsonResponse(json)