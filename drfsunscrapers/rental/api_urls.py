from django.urls import include, path
from .api_routers import router

urlpatterns = [
    path('v1/',include(router.urls)),
]
