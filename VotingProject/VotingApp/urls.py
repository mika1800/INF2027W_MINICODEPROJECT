from django.urls import path
from .import views
import votingAppLandingPage


#Defines routing for functions implemented in views.py
app_name = 'polls'

#URL patterns are equated to a list and this list contains different paths/routes
urlpatterns = [ 
    path ('', views.index, name = 'index' ),#welcome page
    path('login/', votingAppLandingPage.views.user_login, name='login'),
    path('signup/', votingAppLandingPage.views.user_signup, name='signup'),
    path('logout/', votingAppLandingPage.views.user_logout, name='logout'),
    path ('<int:question_id>/', views.detail, name = 'detail'),
    path ('<int:question_id>/results/', views.results, name = 'results'),
    path ('<int:question_id>/vote/', views.vote, name = 'vote'),
]

   