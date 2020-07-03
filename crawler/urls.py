from django.urls import path, re_path
from .views import *

urlpatterns = [
	path('2018/daily/', year_2018),
	path('2019/daily/', year_2019),
	path('2020/daily/', year_2020),
	path('2018/monthly/', year_2018_momthly),
	path('2019/monthly/', year_2019_momthly),
	path('2020/monthly/', year_2020_momthly),
	re_path(r'^dailyreport/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<date>[0-9]{1,2})/$', daily_report),
	path('cron/', cronjob),
]