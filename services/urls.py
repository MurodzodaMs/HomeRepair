from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categoryes', CategoryAPIView, basename='category')

urlpatterns = [

]
urlpatterns.extend(router.urls)