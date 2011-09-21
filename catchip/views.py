# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from catchip.models import IPLog
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import json
def show_all(request):
    context = {}
    context["connect_ip"] = request.META["REMOTE_ADDR"]
    return render_to_response("catchip/show_ip.html", context, RequestContext(request))

def record(request,machine_name):
    if not machine_name:
        return redirect('views.show_all')

    last_ip = IPLog.objects.filter(name=machine_name)
    if len(last_ip) > 0:
        last_ip = last_ip[0]
    else:
        last_ip = None

    new_ip = IPLog(name=machine_name, ip=request.META["REMOTE_ADDR"])
    new_ip.save()

    context = {
        "name": machine_name,
        "last_ip": last_ip or None,
        "new_ip": new_ip.ip,
        "latest_hit": new_ip.last_hit,
    }
    return render_to_response("catchip/record.html", context, RequestContext(request))


def get_ip(request, machine_name):
    if not machine_name:
        return redirect('views.show_all')

    try:
        iplog = IPLog.objects.filter(name=machine_name).latest(field_name='last_hit')
    except IPLog.DoesNotExist:
        raise Http404

    ret = {
        "machine_name" : iplog.name,
        "ip" : iplog.ip,
        "last_updated" : iplog.last_hit.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return HttpResponse(json.dumps(ret))


