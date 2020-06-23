from django.urls import path

from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:session_id>/', views.detail, name='detail'),
    path('<int:session_id>/rate', views.rate, name='rate_session')
]