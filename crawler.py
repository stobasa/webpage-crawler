import re
import os
import wget
import time
import json
import requests
import pandas as pd
import urllib.request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup

homepage = 'https://opentreasury.gov.ng'

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
                        day_report_link.update({column[0].text: ""})
                        
                        
    return day_report_link

def save_dict(dict, name):
    
    with open(str(name), 'w') as fp:
        json.dump(dict, fp, sort_keys=True, indent=4)
    return("File Saved")

def open_json(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        print("Data Saved")
    return data

def request_year(year):

    year_link = open_json("yearlink.json")
    year_url = year_link[str(year)]
    year_file_link = get_file_link(year_url)

    return (year_file_link)

def merge_year_data():
    all_data = {}
    for i in ["2018","2019","2020"]:
        year_data = request_year(i)
        all_data.update(year_data)
        save_dict(all_data, "all_data.json")
    
    return all_data

def get_by_date(date):
    all_data = merge_year_data()
    file_link = all_data[date]

    return file_link

# function to return key for any value 
def get_key(my_dict, val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def download_file(url, name):

    r = requests.get(url, allow_redirects=True, verify=False)
    if url.find('.'):
        extention = (url.rsplit('.', 1)[-1])
        filename = (str(name) + "." + str(extention))
    else:
        filename = name
    with open(filename.replace("/","-"), 'wb') as f:
        f.write(r.content)
        f.close
    

def download_all_file():
    #merge_year_data()
    data = open_json("all_data.json")
    data = pd.DataFrame({"Date": list(data.keys()), "link": list(data.values())})
    for i in range(len(data)):
        if data["link"][i] != "":
            download_file(data["link"][i], data["Date"][i])
    return ("File Downloaded")



if __name__ == "__main__":
    merge_year_data()
    #download_all_file()