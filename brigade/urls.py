from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('', BrigadeAPIViewSet, basename='brigade')

urlpatterns = router.urls

# urlpatterns += router.urls
