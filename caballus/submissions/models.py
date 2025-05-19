from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

class submissionSample(models.Model):
    id = models.IntegerField(primary_key=True, default=None) 
    created_at = models.DateField(default=now) 
    content = models.CharField(max_length=150)
   
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default = None,
        null=True, 
        blank=True,
    )
