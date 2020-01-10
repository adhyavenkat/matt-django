from django.db import models

class News(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    tracking_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id