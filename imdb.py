# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:19:29 2018

@author: Aricent
"""

import scrapy, json, re, openpyxl
my_file = open("C:\\Users\\Aricent\\tutorial\\imdb1.json",'w+')
oscar_2018 = {"Oscars Categories":"Oscar Winners"}

class ParseIMDB(scrapy.Spider):
    name = 'imdb'
    
    
    def start_requests(self):
        urls = [
                'https://www.imdb.com/oscars/nominations/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4395ef7d-6c05-4720-b03d-8d31fc0af5dd&pf_rd_r=412QRQE1Z96VSCF5WKGW&pf_rd_s=top-1&pf_rd_t=60601&pf_rd_i=oscars&ref_=fea_acd_nav_i3'
                ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_imdb)
            
    def parse_imdb(self,response):
        js_output = response.xpath('//span[@class="ab_widget"]//script[@type="text/javascript"]').extract()
        for line in js_output[0]:
            my_file.write(line)    
        self.extract_movie_info()
            
    def extract_movie_info(self):
        print("In function")
        json_file = open("C:\\Users\\Aricent\\tutorial\\imdb1.json")
        my_json_out = open("C:\\Users\\Aricent\\tutorial\\imdb_out.json","w+")
        my_lines = json_file.readlines()
        my_rex = re.compile(r'(?<=\'center-8-react\',)(.*)(?=]\);)')
        for line in my_lines:
            if "center-8-react" in line:
                my_line = my_rex.search(line)
                my_json_out.write(my_line.group())
        my_file = open("C:\\Users\\Aricent\\tutorial\\imdb_out.json")
        json_data = json.load(my_file)
        length = len(json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"])
        print(length)
        
        for i in range(0,24):
            if json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["nominations"][0]["isWinner"]:
                categories = (json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["categoryName"]).upper()
                winners = json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["nominations"][0]["primaryNominees"][0]["name"]
                oscar_2018[categories] = winners
        print(oscar_2018)