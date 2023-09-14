from pytube import YouTube


class Downloader:
    def __init__(self, url, destination_dir):
        self.url = url
        self.destination_dir = destination_dir

    def download(self):
        yt = YouTube(self.url)
        yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(output_path=self.destination_dir)
