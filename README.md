# python-reference-files

#File imdb.py
This script is used to extract java Script part from the source page of Oscar Awards,
  js_output = response.xpath('//span[@class="ab_widget"]//script[@type="text/javascript"]').extract()
  
  The output from this script is used by the below script to get only json content

# File "script to extract exact json content from oscars page"
  Purpose : Regex commands too extract only json content from oscars awards page. Example link is "https://www.imdb.com/oscars/nominations/?"
  Tested succesful
