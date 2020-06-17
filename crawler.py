import wget
import time
import json
import requests
import urllib.request
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()

options = Options()
options.headless = True

homepage = 'https://opentreasury.gov.ng'

def get_year_link():
    
    
    year_dict = {}
    
    
    driver = webdriver.Firefox(options=options)

    # get web page
    driver.get(homepage)


    daily_payment_report = driver.find_element_by_css_selector('.sppb-panel:nth-child(1) > .sppb-panel-heading')

    daily_payment_report.click()

    fg_report = driver.find_element_by_id('sppb-modal-1537891110859-selector')

    fg_report.click()
    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')
    driver.quit()


    tbody = soup_level1.find('tbody')
    table_content= tbody.find_all('td')
    
    for i in table_content:
        _year = i.find('a').text
        _link = homepage + i.find('a')['href']

        year_dict.update({_year: _link})
        
    return year_dict

def get_file_link(url):
    
    day_report_link = {}


    homepage = 'https://opentreasury.gov.ng'

    response = requests.get(url, verify=False)
    soup_level2 = BeautifulSoup(response.text, "html.parser")
    #soup_level2=BeautifulSoup(driver.page_source, 'lxml')
    month_tbody = soup_level2.find_all('tbody')
    table_rows= month_tbody [0].find_all('tr')
    for months in month_tbody:
        table_rows= months.find_all('tr')
        for i in table_rows:
            column = i.find_all('td')
            for j in column:
                if j != None:
                    try:
                        day_report_link.update({column[0].text: homepage + column[1].find('a')['href']})
                        
                    except:
                        day_report_link.update({column[0].text: None})
                        
                        
    return day_report_link

def save_dict(dict, name):
    
    with open(str(name), 'w') as fp:
    json.dump(dict, fp, sort_keys=True, indent=4)
    return("File Saved")

def request_year(year):

    year_link = get_year_link()
    get_file_link = (year_link[year])

    return (get_file_link)

def merge_year_data():
    all_data = {}
    for i in [2018,2019,2020]:
        year_data = request_year(i)
        all_data.update(year_data)
    
    return all_data

def get_by_date(date):
    all_data = merge_year_data()
    file_link = all_data[date]

    return file_link

# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def download_file(url, filename):
    wget.download(url, 'filename')
    return("File downloaded")

def downlaod_all_file():
    for i in merge_year_data().values():
        download_file(i, get_key(i))
    return ("File Downloaded")

