# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:28:28 2018

@author: svrsunil
"""

# -*- coding: utf-8 -*-
from dbhelper import DBHelper

db = DBHelper()

"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup

from urllib.request import Request, urlopen

import json
from datetime import datetime
from selenium import webdriver
import schedule

class check:



    def scarp1(url="",label="eremit"):

        print("scarp1:"+ label)

        q = Request(url)

        q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')

        page = urlopen(q)

        soup = BeautifulSoup(page, 'html.parser')

        #result = str(soup)

        result = json.loads(str(soup))

        for ctr in result['ExchangeRatesList']:

            if('India' in ctr['CountryName']):

               return ctr['ExchangeRate']

               # break;

    def scarp0(url="",label="xe"):

        print("scarp1:"+ label)

        q = Request(url)

        q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')

        page = urlopen(q)

        soup = BeautifulSoup(page, 'html.parser')
        #sp1.find('span', id="exchange-rate-calc")
        return str(soup.select_one("span.uccResultAmount").text)

    def scarp2(url="",label="matchmoney"):

        print('scarp2:'+ label)

        q = Request(url)

        q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')

        page = urlopen(q)

        return BeautifulSoup(page, 'html.parser')



    def scarp3(url="",label = "money2anywhere"):

        print('scarp3:'+ label)
        print('')
        q= Request(url)

        q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
        sp = BeautifulSoup(urlopen(q), 'html.parser')
        print(sp.find('span',id="exchange-rate-calc"))
        browser = webdriver.Firefox()
        browser.get(url)
        html_source = browser.page_source
        browser.quit()

        sp1 = BeautifulSoup(html_source)
        print(sp1.find('span', id="exchange-rate-calc"))

    if __name__ == "__main__":

        start_date = datetime.now()

        xe = scarp0("http://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=INR")
        text =  "\n 1) XE : http://www.xe.com 1 MYR = :" + str(xe)
        eremit = scarp1("https://api.eremit.com.my/EremitService.svc/GetExchangeRates")
        mmrate = scarp2("https://transfer.moneymatch.co/utility/rate/MYR/INR")
        text = text + "\n 2) E-Remit : http://www.eremit.com.my/ 1 MYR = :" + str(eremit)
        text = text + "\n 3) Money Match : https://transfer.moneymatch.co/ 1 MYR = :" + str(mmrate)

        today = str(datetime.today())

        text = text + "\n On " + today
        text = text + "\n All Info are crawled from  net, not for commercial purpose. For Live price visit the site.."
        print(text)
        db.add_info("forex", text, today)
        #scarp3("htadd_infotps://my.uaeexchange.com/")

        print( datetime.now() - start_date)