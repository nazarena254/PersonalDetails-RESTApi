from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.next, name='next'),
    path('api/persons/', views.PersonalDetailsList.as_view(), name='personaldetailsendpoint'),
    path('api/persons/person-id/<int:pk>',
        views.PersonalDetailsDescription.as_view())
    
]