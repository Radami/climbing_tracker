from django.urls import path

from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:session_id>/rate', views.rate, name='rate_session')
]