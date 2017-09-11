from django.http import HttpResponse
import json  

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
	
  
def getUserList(request):  
    response_data = {}  
    response_data['result'] = 'failed'  
    response_data['message'] = 'You messed up'  
    return HttpResponse(json.dumps(response_data), content_type="application/json")  
 