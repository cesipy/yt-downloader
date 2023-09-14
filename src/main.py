import sys
import urllib.parse
import downloader
import os


def handle_cli():
    if len(sys.argv) == 2:
        url = sys.argv[1]
        dl = handle_arguments(url, "downloaded_videos")
        return dl

    elif len(sys.argv) == 3:
        url = sys.argv[1]
        custom_path = sys.argv[2]
        dl = handle_arguments(url, custom_path)
        return dl

    else:
        print(f"incorrect usage! usage: python {sys.argv[0]} <url> ( additional <output path> )")
        sys.exit(1)


def handle_arguments(url: str, path: str) -> downloader.Downloader:
    """
    handles the url and path and returns a downloader object
    
    :return: dl downloader object
    """
    is_valid = valid_url(url)

    if is_valid:
        if os.path.exists(path) and os.path.isdir(path):
            # create downloader object
            dl = downloader.Downloader(url, path)
            return dl

        else:
            print(f"Custom path does not exist or is not a directory: {path}")
            sys.exit(1)
    else:
        print(f"Incorrect url: {url}")
        sys.exit(1)


def valid_url(url: str) -> bool:
    """
    checks if the given url is correct and can be used for the downloader.
    :param url
    :return: bool: whether url is valid or not.
    """
    try:
        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    dl = handle_cli()
    dl.download()


if __name__ == "__main__":
    main()
