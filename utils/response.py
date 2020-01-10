from django.http import JsonResponse

def __http_response__(message = "success", results = {}):
        return JsonResponse({
        "message": message,
        "results" : results
    })