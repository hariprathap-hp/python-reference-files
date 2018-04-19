# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:19:29 2018
@author: Hari Prathap
"""

import scrapy, json, re, os
js_file = " "
oscar_2018 = {"Oscars Categories":"Oscar Winners"}
year = ""

class ParseIMDB(scrapy.Spider):
    name = 'imdb'

    def start_requests(self):   
        urls = [
                'https://www.imdb.com/event/ev0000003/2016/1/?ref_=ev_eh',
                'https://www.imdb.com/event/ev0000003/2017/1/?ref_=ev_eh'
                ]        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_imdb)
            
    def parse_imdb(self,response):
        my_file = open("C:\\Users\\Aricent\\tutorial\\javascript.json",'wb+')
        js_output = response.xpath('//span[@class="ab_widget"]//script[@type="text/javascript"]').extract()
        my_file.write(js_output[0].encode("utf-8"))
        self.extract_movie_info()
            
    def extract_movie_info(self):
        print("In function")
        json_file = open("C:\\Users\\Aricent\\tutorial\\javascript.json")
        my_json_out = open("C:\\Users\\Aricent\\tutorial\\final_json.json","w+")
        my_lines = json_file.readlines()
        #print(my_lines)
        my_rex = re.compile(r'(?<=\'center-(\d)-react\',)(.*)(?=]\);)') 
        for line in my_lines:
            if "nomineesWidgetModel" in line:      
                my_line = my_rex.search(line)
                if my_rex.search(line):
                    print("my_rex")
                else:
                    print("fuck off")
                my_json_out.write(my_line.group())
        my_file = open("C:\\Users\\Aricent\\tutorial\\final_json.json")
        json_data = json.load(my_file)
        length = len(json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"])
        print(length)
        
        for i in range(0,24):
            if json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["nominations"][0]["isWinner"]:
                categories = (json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["categoryName"]).upper()
                winners = json_data["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["nominations"][0]["primaryNominees"][0]["name"]
                oscar_2018[categories] = winners
        print(oscar_2018)
        my_file.close()
        my_json_out.close()
        os.remove("C:\\Users\\Aricent\\tutorial\\javascript.json")
        os.remove("C:\\Users\\Aricent\\tutorial\\final_json.json")
