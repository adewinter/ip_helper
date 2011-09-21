# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def show_all(request):
    context = {}
    
    return render_to_response("catchip/show_ip.html", context, RequestContext(request))