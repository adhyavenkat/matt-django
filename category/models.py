from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=8)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    parent_id = models.IntegerField(editable=False)

    def __str__(self):
        return self.id
