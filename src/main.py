import sys
import urllib.parse
import downloader
import os


def handle_cli_arguments():
    global dl
    length_argv: int = len(sys.argv)
    print(length_argv)

    # only url provided
    if length_argv == 2:
        url: str = sys.argv[1]
        is_valid: bool = valid_argument(url)

        if is_valid:
            dir = os.path.relpath("../downloaded_videos")
            dl = downloader.Downloader(url, dir)

        else:
            print(f"incorrect url: {url}")
            sys.exit()

    # url and path provided
    if length_argv == 3:
        url: str = sys.argv[1]
        is_valid: bool = valid_argument(url)
        path_to_check = sys.argv[2]  # custom dirs

        if os.path.exists(path_to_check):
            dir = os.path.relpath(path_to_check)
        else:
            dir = os.path.relpath("../downloaded_videos")

        if is_valid:
            dl = downloader.Downloader(url, dir)

        else:
            print(f"incorrect url: {url}")

    # incorrect usage
    else:
        print(f"incorrect usage! usage: python {sys.argv[0]} <url to video> ( <destination directory> )")
        sys.exit()

    return dl


def valid_argument(url: str) -> bool:
    try:
        # Attempt to parse the URL
        parsed_url = urllib.parse.urlparse(url)

        # Check if the scheme (e.g., http, https) and netloc (e.g., domain) are not empty
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    dl = handle_cli_arguments()
    dl.download()

main()
