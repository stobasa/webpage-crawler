from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import requests

homepage = 'https://opentreasury.gov.ng'
querystring_2018 = '/index.php/component/content/article/11-dpr/29-daily-payment-report-2?Itemid=101'
querystring_2019 = '/index.php/component/content/article/11-dpr/2759-daily-payment-report-fgn-2019?Itemid=101'
querystring_2020 = '/index.php/component/content/article/11-dpr/3015-2020-daily-payment?Itemid=101'

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

						#print(result, file=open("output.txt", "w"))

		return Response([result])
