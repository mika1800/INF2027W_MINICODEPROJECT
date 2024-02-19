from django.urls import path
from .import views


#Defines routing for functions implemented in views.py
app_name = 'polls'

#URL patterns are equated to a list and this list contains different paths/routes
urlpatterns = [ 
    path ('', views.index, name = 'index' ),#welcome page
    path ('<int:question_id>/', views.detail, name = 'detail'),
    path ('<int:question_id>/results/', views.results, name = 'results'),
    path ('<int:question_id>/vote/', views.vote, name = 'vote'),
]

   