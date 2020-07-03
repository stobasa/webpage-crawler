from django.urls import path, re_path
from .views import *

urlpatterns = [
	path('2018/daily/', year_2018),
	path('2019/daily/', year_2019),
	path('2020/daily/', year_2020),
	path('2018/monthly/', year_2018_momthly),
	path('2019/monthly/', year_2019_momthly),
	path('2020/monthly/', year_2020_momthly),
	path('2018download/', year_2018_download),
	path('2019download/', year_2019_download),
	path('2020download/', year_2020_download),
	re_path('monthlyreport/<int:year>/<str:based>/<str:month>/', monthly_report),
	re_path(r'^dailyreport/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<date>[0-9]{1,2})/$', daily_report),
	
]