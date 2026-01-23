from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', CategoryAPIView, basename='category')
router.register('', ServiceAPIView, basename='service')

urlpatterns = [

]
urlpatterns.extend(router.urls)