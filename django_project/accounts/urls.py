from django.urls import path
from . import views
 

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete/', views.delete, name='delete'),
]