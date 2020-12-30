from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.SessionsIndexView.as_view(), name='index'),
    path('<int:pk>/', views.SessionsDetailView.as_view(), name='detail'),
    path('<int:session_id>/rate', views.rate, name='rate_session'),
    
    path('api/sessions/', views.SessionList.as_view()),
    path('api/sessions/<int:pk>', views.SessionDetails.as_view()),
    path('api/climbs/', views.ClimbList.as_view()),
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)