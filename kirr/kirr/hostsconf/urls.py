from django.urls import path

from .views import wildcard_redirect


urlpatterns = [
    path(r"(?P<path>.*)", wildcard_redirect),

]