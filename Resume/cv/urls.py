from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('university/', educationOne, name='university'),
    path('mba/', educationTwo, name='mba'),
    path('courses/', educationThree, name='courses'),
    path('it_course/', educationFour, name='it'),
    path('assignments/', assignmentsLT, name='assignments'),
    path('assignments_st/', assignmentsST, name='assignments_st'),
]
