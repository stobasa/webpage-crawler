from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import requests
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

homepage = 'https://opentreasury.gov.ng'
querystring_2018 = '/index.php/component/content/article/11-dpr/29-daily-payment-report-2?Itemid=101'
querystring_2019 = '/index.php/component/content/article/11-dpr/2759-daily-payment-report-fgn-2019?Itemid=101'
querystring_2020 = '/index.php/component/content/article/11-dpr/3015-2020-daily-payment?Itemid=101'
querystring_2018_monthly = "/index.php/component/content/article/15-sample/221-monthly-budget-performance-fgn-total?Itemid=101"
querystring_2019_monthly ="/index.php/component/content/article/54-2019/fgn-monthly/1212-fgn-monthly?Itemid=101"
querystring_2019_monthly = "/index.php/component/content/article/92-2020/3847-fgn-monthly?Itemid=101"

CRON_URL = "http://localhost:8080/v1/dailyreport"
CRON_TIME = "09:00"

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
def year_2018_download(request):
	"""
	Download the excel files (.xlsx) of 2018
	:param request:
	:return: filename, download url
	"""
	result = []
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
								file_name = table_data[0].text
								file_link = homepage + table_data[1].find('a')['href']
								result.append({file_name: file_link})
								
								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type
								# print("Downloading...")
								with open('excel_sheets/2018/{}'.format(excel_file), 'wb') as file:
									response = requests.get(file_link, verify=False)
									file.write(response.content)
							
							except:
								result.append({table_data[0].text: ""})
		print("The end")
		return Response([result])


@api_view(['GET'])
def year_2019_download(request):
	"""
	Download the excel files (.xlsx) of 2019
	:param request:
	:return: filename, download url
	"""
	result = []
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
								file_name = table_data[0].text
								file_link = homepage + table_data[1].find('a')['href']
								result.append({file_name: file_link})
								
								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type
								# print("Downloading...")
								with open('excel_sheets/2019/{}'.format(excel_file), 'wb') as file:
									response = requests.get(file_link, verify=False)
									file.write(response.content)
							
							except:
								result.append({table_data[0].text: ""})
		print("The end")
		return Response([result])


@api_view(['GET'])
def year_2020_download(request):
	"""
	Download the excel files (.xlsx) of 2020
	:param request:
	:return: filename, download url
	"""
	result = []
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
								file_name = table_data[0].text
								file_link = homepage + table_data[1].find('a')['href']
								result.append({file_name: file_link})
								
								# rename the file, save it's extension and download
								excel_file_name = file_name.replace('/', '_')
								excel_file_type = file_link.split('.')[-1]
								excel_file = excel_file_name + '.' + excel_file_type
								# print("Downloading...")
								with open('excel_sheets/2020/{}'.format(excel_file), 'wb') as file:
									response = requests.get(file_link, verify=False)
									file.write(response.content)
							
							except:
								result.append({table_data[0].text: ""})
		print("The end")
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
		return Response("Invalid date")


# Run Cron Jobs
def cronjob(request):
	import schedule
	import time 

	schedule.every().day.at(CRON_TIME).do(job)
	# schedule.every(10).seconds.do(job)
	while True:
		schedule.run_pending()
		time.sleep(1)


def job():
	x = datetime.datetime.now()

	year =  str(x.year)

	month  = str(x.month)
	if len(month) == 1:
		month = "0"+ str(x.month)

	day = x.day
	if len(year) == 1:
		day = "0" + str(x.day)

	re = requests.get(CRON_URL+'/{}/{}/{}/'.format(year,month, day)).text

	soup = BeautifulSoup(re,'lxml')
	link = soup.find('pre', class_ = 'prettyprint').find('a')['href']

	return JsonResponse([link], safe=False)



