from django.db import models
from django.utils.timezone import now

class sunmission_sample(models.Model):
    id = models.IntegerField(primary_key=True, default=None) 
    created_at = models.DateField(default=now) 
    content = models.CharField(max_length=150)
   
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

