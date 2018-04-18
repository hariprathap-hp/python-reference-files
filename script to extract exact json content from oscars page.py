# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:23:50 2018

@author: Aricent
"""

import re

def main():
    my_file = open("C:\\Users\\Aricent\\tutorial\\imdb1.json")
    my_out = open("C:\\Users\\Aricent\\tutorial\\imdb_out.json","w+")
    my_lines = my_file.readlines()
    print(len(my_lines))
    my_rex = re.compile(r'(?<=\'center-8-react\',)(.*)(?=]\);)')
    for line in my_lines:
        if "center-8-react" in line:
            my_line = my_rex.search(line)
            print(my_line)
            my_out.write(my_line.group())

if __name__ == "__main__":
    main()
