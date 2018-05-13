from django.db import models

# Create your models here.

class Server(models.Model):
    METHOD_CHOICES = (
        ("GET","GET"),
        ("POST","POST"),
    )

    url = models.CharField(max_length=200)
    method = models.CharField(max_length=5, choices=METHOD_CHOICES, default="GET")
    content = models.CharField(max_length=200, blank=True, null=True)
    headers = models.CharField(max_length=200, blank=True, null=True)
    response = models.CharField(max_length=200)
    success_times = models.IntegerField(default=0)
    failed_times = models.IntegerField(default=0)
    last_fail = models.TextField(blank=True, null=True)


class Phone(models.Model):
    number = models.CharField(max_length=15)
    active_time = models.DateTimeField()

