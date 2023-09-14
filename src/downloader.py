from pytube import YouTube


class Downloader:
    def __init__(self, url, destination_dir):
        self.url = url
        self.destination_dir = destination_dir

