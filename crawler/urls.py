from django.urls import path
from .views import *

urlpatterns = [
	path('2018/', year_2018),
	path('2019/', year_2019),
	path('2020/', year_2020),
]