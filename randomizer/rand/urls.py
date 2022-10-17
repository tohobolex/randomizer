from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('', index),
    path('homesimply', homesimply),
    path('simplyrand', simplyrand),
    path('allrecipes/all', allrecipes),
    path('allrecipes/category/<name>', category1),
    path('allrecipes/cuisine/<name>', cuisine1),
    path('allrecipes/difficulty/<name>', difficulty1),
    path('randomizer', testrand),
    path('comments', comments)
]