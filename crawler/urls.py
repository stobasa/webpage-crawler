from django.urls import path
from .views import *

urlpatterns = [
	path('2018/', year_2018),
	path('2019/', year_2019),
	path('2020/', year_2020),
	path('2018monthly/', year_2018_momthly),
	path('2019monthly/', year_2019_momthly),
	path('2020monthly/', year_2020_momthly),
	path('2018download/', year_2018_download),
	path('2019download/', year_2019_download),
	path('2020download/', year_2020_download),
]