from django.urls import include, path

urlpatterns = [
    path('api/',include('rental.api_urls')),
]
