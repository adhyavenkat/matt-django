# from django.test import TestCase
# from pkg_resources import require
# from rest_framework import status
# from rest_framework.generics import (ListCreateAPIView,
#                                      RetrieveUpdateDestroyAPIView)
# from rest_framework.response import Response

# from category.views import get_post_category


# class CategoryTestCase(TestCase):

#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

#     def test_get_category_data(self):
#         """get category records"""
#         request = "<rest_framework.request.Request object at 0x10be42e10>"
#         response = get_post_category.get(self, request)
#         print("MM",response)


from rest_framework.test import RequestsClient
from django.test import TestCase



class CategoryTestCase(TestCase):

    def test_get_category_data(self):
        
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/category/')
        print(response.status_code)
        print(type(response.status_code))
        assert response.status_code == 200