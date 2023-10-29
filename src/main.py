import sys
import urllib.parse
import os
from rich.console import Console
from rich.prompt import Prompt
from downloader import Downloader
from rich.table import Table
from rich.panel import Panel

# global console for the rich output
console = Console()


def run_download(url: str, path: str) -> str:
    """
    downloads the video of a given url and path.
    returns the path of the downloaded file (if successful).

    :param url: url of youtube video
    :param path: path to save the downloaded video to
    :return: path of the downloaded file.
    """
    dl = handle_arguments(url, path)
    result = dl.download()

    return result


def handle_cli():
    # switch to terminal interface mode
    if len(sys.argv) == 1:
        rich_text_interface()
        sys.exit(0)

    # url to video is provided
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        dl = handle_arguments(url, "downloaded_videos")
        return dl

    # url and custom path are provided
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        custom_path = sys.argv[2]
        dl = handle_arguments(url, custom_path)
        return dl

    # incorrect usage
    else:
        console.print(f"[red]Incorrect usage![/red] Usage: [green]python {sys.argv[0]} <url> ( additional <output path> )[/green]")
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
            console.print(f"[red]Custom path does not exist or is not a directory:[/red] {path}")
            sys.exit(1)
    else:
        console.print(f"[red]Incorrect URL:[/red] {url}")
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
    """
    simple interface for the youtube downloader.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    console.print(Panel("[bold green]YouTube Downloader[/bold green]", title="Welcome", border_style="green"))

    url = Prompt.ask("[bold]Enter the YouTube video URL[/bold]")
    output_path = Prompt.ask(
        "[bold]Enter the output path (or press Enter for 'downloaded_videos'): [/bold]", default="downloaded_videos")

    # saving path to result
    result = run_download(url, output_path)

    # Create a table to display user input
    input_table = Table.grid(padding=(0, 2))
    input_table.add_column(justify="right")
    input_table.add_column()
    input_table.add_row("[bold]Video URL:[/bold]", f"[blue]{url}[/blue]")
    input_table.add_row("[bold]Output Path:[/bold]", f"[blue]{output_path}[/blue]")

    console.print(input_table)
    console.print(Panel("[cyan]Downloading video...[/cyan]", title="Status", border_style="blue"))
    console.print(Panel("[bold green]Download complete![/bold green]", title="Status", border_style="green"))
    console.print("[bold italic]saved to: ", result, "\n")


def main():
    dl = handle_cli()
    dl.download()


if __name__ == "__main__":
    main()
