from django.urls import path
from . import views


urlpatterns = [
    path('api/conversion-rate/', views.conversion_rate, name='conversion_rate'),
    path('api/status-distribution/', views.status_distribution, name='status_distribution'),
    path('api/category-type-performance/', views.category_type_performance, name='category_type_performance'),
    path('api/filtered-aggregation/', views.filtered_aggregation, name='filtered_aggregation'),
]
