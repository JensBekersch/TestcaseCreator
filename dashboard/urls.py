from dashboard.views import front_page

from django.urls import path

urlpatterns = [
    path('', front_page, name='front_page'),
]
