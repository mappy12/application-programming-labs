from icrawler.builtin import GoogleImageCrawler

def download_cats(keyword: str, num: int, dir: str):

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=6,
        storage={'root_dir': dir}
    )

    google_crawler.crawl(keyword=keyword, max_num=num)