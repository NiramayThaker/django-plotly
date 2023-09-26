from django.urls import path
from . import views


urlpatterns = [
    path('line-chart/', views.charts, name='chart'),
]
