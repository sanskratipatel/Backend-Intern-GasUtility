# support/models.py

from django.db import models

class SupportRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
    ]

    request_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    request_details = models.TextField()
    status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_details} - {self.status}"