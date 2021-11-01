import time

import click
import tqdm

import py4cdl


@click.command()
@click.argument("url")
@click.option("--dest-dir", default=".", show_default=True, help="Destination directory for media files")
def main_4cdl(url, dest_dir):
    """Download media from URL."""
    page = py4cdl.webpage.obtain_webpage(url)
    links = py4cdl.image_links.get_image_links_and_names(page)

    for x in tqdm.tqdm(links):
        time.sleep(5)
        py4cdl.download.download_media(x[0], x[1], x[2], dest_dir)

if __name__ == "__main__":
    main_4cdl()

