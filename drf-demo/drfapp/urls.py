from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from .views import StudentViewSet, UniversityViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documentation')

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    path('docs/', schema_view, name="docs"),
]

urlpatterns += router.urls
