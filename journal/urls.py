from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:session_id>/rate', views.rate, name='rate_session'),
    path('api_sessions', views.session_list, name='api_sessions_list'),
    path('api_sessions/<int:pk>', views.session_details, name='api_sessions_details')
]

urlpatterns = format_suffix_patterns(urlpatterns)