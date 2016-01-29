__author__ = 'Rfun'

from crawler.Downloader import *
from crawler.parser import *
from crawler.item_pipeline import *
from crawler.scheduler import *

max_articles = 1000

def crawl_articles():
    scheduler = Scheduler()
    item_pipeline = ItemPipeline(scheduler)
    while item_pipeline.get_items_len() < max_articles:
        print('\r %% %.2 of the total work' %(item_pipeline.get_items_len()*100/max_articles))
        try:
            next_url = scheduler.get_new_url()
            pprint('next url is %s' % next_url)
            downloaded = download_url(next_url)
            if downloaded is not None:
                parsed = parse(downloaded)
                item_pipeline.add_items(parsed)
                print('now the item len is : %d' % item_pipeline.get_items_len())
        except:
            traceback.print_exc()

    item_pipeline.save_to_text_file()
    item_pipeline.pickle_graph()

def crawl_author():
    scheduler = Scheduler()
    item_pipeline = ItemPipeline(scheduler)
    while item_pipeline.get_items_len() < max_articles:
        try:
            pass
        except:
            pass

def main():

    # print(item_pipeline.get_graph())

if __name__ == '__main__':
    main()