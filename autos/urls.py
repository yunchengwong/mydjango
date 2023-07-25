from django.urls import path
from . import views

app_name = 'autos'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('main/create/', views.AutoCreateView.as_view(), name='autoCreate'),
    path('main/<int:pk>/update/', views.AutoUpdateView.as_view(), name='autoUpdate'),
    path('main/<int:pk>/delete/', views.AutoDeleteView.as_view(), name='autoDelete'),
    path('lookup/', views.MakeView.as_view(), name='make'),
    path('lookup/create/', views.MakeCreate.as_view(), name='makeCreate'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='makeUpdate'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='makeDelete'),
]