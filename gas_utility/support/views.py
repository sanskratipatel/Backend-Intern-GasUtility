# support/views.py

from django.shortcuts import render
from .models import SupportRequest
def support_home(request):
    # Option 1: Render a simple template
    return render(request, 'support/support_home.html')

def request_list(request):
    requests = SupportRequest.objects.all()
    return render(request, 'support/request_list.html', {'requests': requests})

def request_detail(request, pk):
    request = SupportRequest.objects.get(pk=pk)
    return render(request, 'support/request_detail.html', {'request': request})