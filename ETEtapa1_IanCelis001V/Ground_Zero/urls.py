from django.urls import path
from .views import index, index2, index4, index5, index6




urlpatterns = [
    path('', index, name="index")
    ,path('index2', index2, name="index2"),path('index', index, name="index")
    ,path('index4', index4, name="index4"),path('index', index, name="index")
    ,path('index5/<id>', index5, name="index5"),path('index', index, name="index")
    ,path('index6/<id>', index6, name="index6"),path('index', index, name="index")
]