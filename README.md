# python-reference-files
script "script to extract exact json content from oscars page"
  Purpose : Regex commands too extract only json content from oscars awards page. Example link is "https://www.imdb.com/oscars/nominations/?"
  Tested succesful
  
#Command 1:
This command is used to extract java Script part from the source page of Oscar Awards,
  js_output = response.xpath('//span[@class="ab_widget"]//script[@type="text/javascript"]').extract()
