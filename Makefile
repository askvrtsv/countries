clean:
	rm -f countries.csv

country: clean
	pipenv run scrapy crawl country -o countries.csv
