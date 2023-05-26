from django.urls import path
from dolar import views

urlpatterns = [
    path('', views.DolarListView.as_view(), name='dolares'),
    path('api/dolares/', views.DolarListAPIView.as_view(), name='api-dolares'),
]
