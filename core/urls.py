from django.urls import path
from . import views


urlpatterns = [
    path('line-chart/', views.charts, name='chart'),
    path('avg-chart/', views.yearly_avg_co2, name='avg-chart'),
]
