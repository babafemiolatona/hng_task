from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(["GET"])
def info_list(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin":"*"}
    info = {
        "slackUsername":"outsider",
        "backend":True,
        "age": 27,
        "bio":"I'm a backend developer"
  }
    return JsonResponse(info, headers=header)