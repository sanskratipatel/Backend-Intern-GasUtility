from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('INSTALLATION', 'Installation'),
        ('REPAIR', 'Repair'),
        ('BILLING', 'Billing Inquiry'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.service_type} - {self.status}"
# Create your models here.
