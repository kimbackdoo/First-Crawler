import crawl

class Starter:
    def __init__(self, product_name_list):
        crawling = crawl.Crawl()
        crawling.start(product_name_list)