from django.db import models
from category.models import Category
from news.models import News

class NewsCategoryRelation(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.BooleanField(default=False)
