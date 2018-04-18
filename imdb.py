# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:19:29 2018

@author: Aricent
"""

import scrapy
my_file = open("C:\\Users\\Aricent\\tutorial\\imdb1.json",'w+')

class ParseIMDB(scrapy.Spider):
    name = 'imdb'
    
    
    def start_requests(self):
        urls = [
                'https://www.imdb.com/oscars/nominations/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4395ef7d-6c05-4720-b03d-8d31fc0af5dd&pf_rd_r=412QRQE1Z96VSCF5WKGW&pf_rd_s=top-1&pf_rd_t=60601&pf_rd_i=oscars&ref_=fea_acd_nav_i3'
                ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        js_output = response.xpath('//span[@class="ab_widget"]//script[@type="text/javascript"]').extract()
        for line in js_output[0]:
            my_file.write(line)    
        yield{
                'link':js_output[0]
                }
        
        '''self.get_God(link)
        
    def get_God(self, titles):
        print(titles)
        for title in titles:
            if 'Dark' in title:
                print(title)'''