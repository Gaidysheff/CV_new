from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('university/', views.educationOne, name='university'),
    path('mba/', views.educationTwo, name='mba'),
    path('courses/', views.educationThree, name='courses'),
    path('it_course/', views.educationFour, name='it'),
    path('assignments/', views.assignmentsLT, name='assignments'),
    path('assignments_st/', views.assignmentsST, name='assignments_st'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_createx/', views.portfolio_createx, name='portfolio_createx'),
    path('portfolio_finsweet/', views.portfolio_finsweet, name='portfolio_finsweet'),
]
