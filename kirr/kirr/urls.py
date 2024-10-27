from django.contrib import admin
from django.urls import path

from shortener.views import HomeView, URLRedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    path("<slug:shortcode>/", URLRedirectView.as_view(), name="scode"),
    #path(r'^(?<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
]
