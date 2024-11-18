
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required

def request_form(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/request_form.html', {'form': form})

def request_status_view(request):
    return render(request, 'customers/request_status.html')
def customers_view(request):
    return render(request, 'customers/request_form.html') 