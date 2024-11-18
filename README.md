# Backend-Intern-GasUtility  
Gas Utility Customer Service Application
Overview
This Django application is designed for a gas utility company to handle a high volume of customer service requests efficiently. It provides tools for customers to submit service requests, track their progress, and view account information. Additionally, it equips customer support representatives with tools to manage and resolve requests.

Features
Customer Features
Service Requests:

Submit online requests for services like gas connection, maintenance, and billing inquiries.
Attach files or images to provide additional details.
Request Tracking:

View the current status of submitted requests.
Track submission and resolution dates.
Account Information:

View personal account details such as name, address, and recent billing history.
Support Representative Features
Request Management:

View a list of all pending and resolved service requests.
Access detailed information about each request.
Resolution Tools:

Update the status of requests to provide real-time updates to customers.
Application Structure  
gas_utility/
│
├── manage.py                         # Django's management script
├── gas_utility/                      # Main project directory
│   ├── __init__.py
│   ├── settings.py                   # Project settings
│   ├── urls.py                       # Project-level URL configurations
│   ├── wsgi.py                       # Web server gateway interface
│   └── asgi.py                       # Asynchronous server gateway interface
│
├── customers/                        # Customer app
│   ├── migrations/                   # Database migrations for customers app
│   ├── __init__.py
│   ├── admin.py                      # Customer models admin configuration
│   ├── apps.py                       # Customer app configuration
│   ├── models.py                     # Models for customer service requests
│   ├── forms.py                      # Django forms for customer inputs
│   ├── views.py                      # Customer-related views (logic)
│   ├── urls.py                       # URL routing for customers app
│   └── templates/
│       └── customers/                # HTML templates for customers
│           ├── request_form.html     # Form for submitting service requests
│           ├── request_status.html   # Request tracking page
│           └── account_info.html     # Page for viewing account information
│
├── support/                          # Support app
│   ├── migrations/                   # Database migrations for support app
│   ├── __init__.py
│   ├── admin.py                      # Support models admin configuration
│   ├── apps.py                       # Support app configuration
│   ├── models.py                     # Models for support request management
│   ├── views.py                      # Support-related views (logic)
│   ├── urls.py                       # URL routing for support app
│   └── templates/
│       └── support/                  # HTML templates for support
│           ├── request_list.html     # List of all service requests
│           └── request_detail.html   # Detailed view of a specific request
│
└── static/                           # Static files for the project
    ├── css/                          # Stylesheets
    ├── js/                           # JavaScript files
    └── images/                       # Static images

Setup and Installation
Prerequisites
Python 3.10+
Django 5.1.3
A database (SQLite is used by default, but can be configured for PostgreSQL or MySQL)
Installation Steps
1. Clone the Repository:
git clone https://github.com/yourusername/gas_utility.git
cd gas_utility
Set up a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Application: Open your browser and navigate to http://127.0.0.1:8000.

Code Highlights
Models (customers/models.py)
Defines the ServiceRequest model with fields for request type, description, attachments, and status.

python
Copy code
class ServiceRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
Forms (customers/forms.py)
Defines a Django form for the service request submission.

python
Copy code
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'request_type', 'description', 'attachment']
Views (customers/views.py)
Handles the business logic for customers.

python
Copy code
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/request_form.html', {'form': form})
Future Enhancements
Authentication: Add user authentication for secure access to account information.
Notifications: Implement email or SMS notifications for request updates.
Dashboard: Create an admin dashboard for better request management.
License
This project is licensed under the MIT License. See the LICENSE file for details.

