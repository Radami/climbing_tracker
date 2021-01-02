from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views, api_views

app_name = 'journal'
urlpatterns = [
    path('', views.SessionsIndexView.as_view(), name='index'),
    path('<int:pk>/', views.SessionsDetailView.as_view(), name='detail'),
    path('add_session', views.add_session, name='add_session'),
    path('<int:session_id>/rate', views.rate, name='rate_session'),
    
    path('api/sessions/', api_views.SessionList.as_view()),
    path('api/sessions/<int:pk>', api_views.SessionDetails.as_view()),
    path('api/climbs/', api_views.ClimbList.as_view()),
    path('api/users/', api_views.UserList.as_view()),
    path('api/users/<int:pk>/', api_views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)