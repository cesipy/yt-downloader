import sys
import urllib.parse
import downloader
import os


def handle_cli_arguments():
    length_argv = len(sys.argv)

    # Correct number of arguments: url only
    if length_argv == 2:
        url = sys.argv[1]
        is_valid = valid_argument(url)

        if is_valid:
            # path = os.path.relpath("downloaded_videos", "yt-downloader")
            path = "downloaded_videos"
            dl = downloader.Downloader(url, path)
            return dl
        else:
            print(f"Incorrect url: {url}")
            sys.exit(1)

    # Correct number of arguments: url and custom path
    elif length_argv == 3:
        url = sys.argv[1]
        is_valid = valid_argument(url)
        custom_path = sys.argv[2]

        if is_valid:
            if os.path.exists(custom_path) and os.path.isdir(custom_path):
                dl = downloader.Downloader(url, custom_path)
                return dl
            else:
                print(f"Custom path does not exist or is not a directory: {custom_path}")
                sys.exit(1)
        else:
            print(f"Incorrect url: {url}")
            sys.exit(1)

    # Incorrect usage
    else:
        print(f"Incorrect usage! Usage: python {sys.argv[0]} <url to video> ( <destination directory> )")
        sys.exit(1)


def valid_argument(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    dl = handle_cli_arguments()
    dl.download()


if __name__ == "__main__":
    main()
