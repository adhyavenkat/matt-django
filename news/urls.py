from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('api/v1/news/', # urls list all and create new one
        views.get_post_news.as_view(),
        name='get_post_news'
    )
]