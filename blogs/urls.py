from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, TagViewSet


router = DefaultRouter()

router.register(r'posts', BlogViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
