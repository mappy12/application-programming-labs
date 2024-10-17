import os.path

from icrawler.builtin import GoogleImageCrawler

def download_cats(keyword: str, num: int, path: str) -> None:

    """
    A function that downloads photos of cats and saves them to the specified path

    :param keyword: Keyword to search
    :param num: Number of photos downloaded
    :param path: Directory where photos are downloaded
    """

    if not os.path.exists(path):
        os.mkdir(path)

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=6,
        storage={'root_dir': path}
    )

    google_crawler.crawl(keyword=keyword, max_num=num)
