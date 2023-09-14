import sys
import urllib.parse
import os
from rich.console import Console
from rich.prompt import Prompt
from downloader import Downloader


def run_download(url, path):
    dl = handle_arguments(url, path)
    dl.download()


def handle_cli():
    if len(sys.argv) == 1:
        rich_text_interface()
        sys.exit(0)
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        dl = handle_arguments(url, "downloaded_videos")
        return dl
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        custom_path = sys.argv[2]
        dl = handle_arguments(url, custom_path)
        return dl
    else:
        print(f"[red]Incorrect usage![/red] Usage: [green]python {sys.argv[0]} <url> ( additional <output path> )[/green]")
        sys.exit(1)


def handle_arguments(url: str, path: str) -> Downloader:
    """
    handles the url and path and returns a downloader object

    :return: dl downloader object
    """
    is_valid = valid_url(url)

    if is_valid:
        if os.path.exists(path) and os.path.isdir(path):
            # create downloader object
            dl = Downloader(url, path)
            return dl
        else:
            print(f"[red]Custom path does not exist or is not a directory:[/red] {path}")
            sys.exit(1)
    else:
        print(f"[red]Incorrect URL:[/red] {url}")
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


def rich_text_interface():
    console = Console()
    console.print("[bold green]YouTube Downloader[/bold green]")
    url = Prompt.ask("[bold]Enter the YouTube video URL:[/bold]")
    output_path = Prompt.ask(
        "[bold]Enter the output path (or press Enter for 'downloaded_videos'): [/bold]", default="downloaded_videos")
    run_download(url, output_path)

    console.print(f"[cyan]Downloading video from URL:[/cyan] [blue]{url}[/blue]")

    console.print(f"[bold green]Video downloaded to:[/bold green] [blue]{output_path}[/blue]\n")


def main():
    dl = handle_cli()
    dl.download()


if __name__ == "__main__":
    main()
