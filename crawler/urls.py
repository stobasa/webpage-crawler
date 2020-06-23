from django.urls import path
from .views import *

urlpatterns = [
	path('2018/', year_2018),
	path('2019/', year_2019),
	path('2020/', year_2020),

	# Months Per Year
	path('2018/month/<int:id>', year_month_2018),
	path('2019/month/<int:id>', year_month_2019),
	path('2020/month/<int:id>', year_month_2020),

	# Day
	path('2018/month/<int:id>/daily/<int:id>', year_month_daily2018),
	path('2019/month/<int:id>/daily/<int:id>', year_month_daily2019),
	path('2020/month/<int:id>/daily/<int:id>', year_month_daily2020),

	# cron
	path('cron/', cron),

]