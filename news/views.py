from django.core.paginator import Paginator
from django.views import View
from rest_auth.app_settings import serializers
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.serializers import Serializer

import category
from newscategoryrelation.models import NewsCategoryRelation
from newscategoryrelation.serializers import MapperCategorySerializer

from .models import News
from .pagination import CustomPagination
from .serializers import NewsSerializer
from utils.response import __http_response__


class get_post_news(ListCreateAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       news = News.objects.all()
       return news

    def get(self, request, *args, **kwargs):
        # get particular category_id news records
        category_id = self.request.GET.get('category_id')
        if category_id:
            data_app = []
            mapper_response = NewsCategoryRelation.objects.filter(category_id=category_id).values_list('news_id', flat=True)
            for response in mapper_response:
                queryset = News.objects.filter(id=response)
                serializer = NewsSerializer(queryset, many=True)
                data_app = data_app + serializer.data
            return __http_response__("success",data_app)
        elif not category_id:
            # get all news records
            news = self.get_queryset()
            paginate_queryset = self.paginate_queryset(news)
            serializer = self.serializer_class(paginate_queryset, many=True)
            return self.get_paginated_response(serializer.data)
            

    