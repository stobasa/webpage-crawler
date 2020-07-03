from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
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
querystring_2020_monthly = "/index.php/component/content/article/92-2020/3847-fgn-monthly?Itemid=101"

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
		return Response("Invaid date")



@api_view(['GET'])
def monthly_report(year, based, month):
	"""
	Monthly report view
	:param request: Year, Based, Month
	Year: Search Year in YYYY format
	Based: Admin for ADMINISTRATIVE SEGMENT, Eco for ECONOMIC CLASSIFICATION and Func for FUNCTIONS OF GOVERNMENT
	Month: Search Month in Format January...
	:return: the download link for the particular month based on it ADMINISTRATIVE SEGMENT,  ECONOMIC CLASSIFICATION or FUNCTIONS OF GOVERNMENT	
	"""

	try:
		if int(year) == 2018:
			url = f'{homepage + querystring_2018_monthly}'
		if int(year) == 2019:
			url = f'{homepage + querystring_2019_monthly}'
		if int(year) == 2020:
			url = f'{homepage + querystring_2020_monthly}'
		

		r = requests.get(url, verify=False).text
		month_dict = {"Admin":{}, "Eco":{}, "Func":{}}

		soup = BeautifulSoup(r, 'lxml')

		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[0].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									month_dict["Admin"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[1].find('a')['href']})
								except:
									result = {table_data[0].text: ""}


		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[1].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									month_dict["Eco"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[1].find('a')['href']})
								except:
									result = {table_data[0].text: ""}


		for section in soup.find('section', attrs={'class': 'sppb-section'}):
			table = section.find_all('table')

		table_rows = table[2].find_all('tr')
		for td in table_rows:
			table_data = td.find_all('td')
			for i in table_data:
							if i != None:
								try:
									month_dict["Func"].update({(table_data[0].text).split(" ")[0]: homepage + table_data[1].find('a')['href']})
								except:
									result = {table_data[0].text: ""}
									
									
		if based == "Admin":
			try:
				result = (month_dict["Admin"][month])
				return Response([result])
			except:
				return Response(["Invalid"])
				
		elif based == "Eco":
			try:
				result = (month_dict["Eco"][month])
				return Response([result])
			except:
				return Response(["Invalid"])
		elif based == "Func":
			try:
				result = (month_dict["Func"][month])
				return Response([result])
			except:
				return Response(["Invalid"])
				
		else:
			return Response(["Invalid"])

	except:
		return Response(["Invalid"])