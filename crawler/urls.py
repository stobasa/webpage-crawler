from django.urls import path, re_path
from .views import *

urlpatterns = [
	path('2018/daily/', year_2018),
	path('2019/daily/', year_2019),
	path('2020/daily/', year_2020),
	path('2018/monthly/', year_2018_momthly),
	path('2019/monthly/', year_2019_momthly),
	path('2020/monthly/', year_2020_momthly),
	path('2018/treasury/monthly', treasury_2018),
	path('2019/treasury/monthly', treasury_2019),
	path('2020/treasury/monthly', treasury_2020),

	path('monthlyreport/<int:year>/<str:based>/<str:month>/', monthly_report),
	re_path(r'^dailyreport/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<date>[0-9]{1,2})/$', daily_report),
	re_path(r'^dailyreportjson/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<date>[0-9]{1,2})/$', daily_report_json),
	re_path(r'^dailytreasuryreport/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<date>[0-9]{1,2})/$', daily_report),

	path('cron/', cronjob),


	# Downloads 
	path('2018/download/', year_download_2018),
	path('2019/download/', year_download_2019),
	path('2020/download/', year_download_2020),

	path('2018/monthly/download/', year_2018_momthly_download),
	path('2019/monthly/download/', year_2019_momthly_download),
	path('2020/monthly/download/', year_2020_momthly_download),

]