from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

homepage = 'https://opentreasury.gov.ng'
querystring_2018 = '/index.php/component/content/article/11-dpr/29-daily-payment-report-2?Itemid=101'
querystring_2019 = '/index.php/component/content/article/11-dpr/2759-daily-payment-report-fgn-2019?Itemid=101'
querystring_2020 = '/index.php/component/content/article/11-dpr/3015-2020-daily-payment?Itemid=101'
querystring_2018_monthly = "/index.php/component/content/article/15-sample/221-monthly-budget-performance-fgn-total?Itemid=101"
querystring_2019_monthly ="/index.php/component/content/article/54-2019/fgn-monthly/1212-fgn-monthly?Itemid=101"
querystring_2019_monthly = "/index.php/component/content/article/92-2020/3847-fgn-monthly?Itemid=101"

@api_view(['GET'])
def year_2018(request):
	url = f'{homepage + querystring_2018}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2019(request):
	url = f'{homepage + querystring_2019}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2020(request):
	url = f'{homepage + querystring_2020}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2018_momthly(request):
	url = f'{homepage + querystring_2018_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[2].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2019_momthly(request):
	url = f'{homepage + querystring_2019_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[2].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])


@api_view(['GET'])
def year_2020_momthly(request):
	url = f'{homepage + querystring_2020_monthly}'
	if request.method == 'GET':
		r = requests.get(url, verify=False).text

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')
			for tr in table:
				table_rows = tr.find_all('tr')
				for td in table_rows:
					table_data = td.find_all('td')
					for i in table_data:
						if i != None:
							try:
								result = {table_data[0].text: homepage + table_data[2].find('a')['href']}
							except:
								result = {table_data[0].text: ""}
		return Response([result])

@api_view(['GET'])
def daily_report(request, year, month, date):
	
	"""
	Daily report view
	:param request: Year, Month, Date
	:return: the download link for the particular day
	"""

	try:
		if int(year) == 2018:
			url = f'{homepage + querystring_2018}'
		if int(year) == 2019:
			url = f'{homepage + querystring_2019}'
		if int(year) == 2020:
			url = f'{homepage + querystring_2020}'
		
		if request.method == 'GET':
			r = requests.get(url, verify=False).text
			soup = BeautifulSoup(r, 'lxml')
			for section in soup.find('section', attrs={'class': 'sppb-section'}):
				for div in section.find_all('div', attrs={'class': 'sppb-panel'})[int(month) - 1]:
					table = div.find_all('table')
					
					for table_rows in table:
						for tr in table_rows.find_all("tr")[int(date) : int(date)+1]:
							table_data = tr.find_all('td')
							for i in table_data:
								if i != None:
									try:
										result = {table_data[0].text: homepage + table_data[1].find('a')['href']}
									except:
										result = {table_data[0].text: ""}
			return Response([result])
		
	except:
		return Response("Invaid date")
