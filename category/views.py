from fnmatch import filter

from pkg_resources import require
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from .models import Category
from .pagination import CustomPagination
from .serializers import CategorySerializer


class get_post_category(ListCreateAPIView):
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        category = Category.objects.filter(status= True).order_by('name')
        return category

    # Get all active category records
    def get(self, request):
        category = self.get_queryset()
        paginate_queryset = self.paginate_queryset(category)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)
