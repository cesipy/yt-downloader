from pytube import YouTube


class Downloader:
    """
    Downloader object
    """
    def __init__(self, url, destination_dir):
        self.url = url
        self.destination_dir = destination_dir

    def download(self) -> str:
        """
        downloads the video from self.url to self.destination_dir.

        :return: result - abs. path to the downloaded file.
        """
        yt = YouTube(self.url)
        result = yt.streams.filter(progressive=True, file_extension="mp4")\
            .order_by("resolution")\
            .desc()\
            .first()\
            .download(output_path=self.destination_dir)
        # return path of downloaded video
        return result
