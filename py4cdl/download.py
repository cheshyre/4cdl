import urllib.request
import pathlib


def download_media(file_link, file_name, file_id, dest_dir=""):
    if dest_dir == "":
        path = pathlib.Path(".")
    else:
        path = pathlib.Path(dest_dir)

    if not path.exists():
        path.mkdir(parents=True)

    file_ext = file_name.split(".")[-1]
    file_no_ext = ".".join(file_name.split(".")[:-1])
    full_file_name = "{}.{}.{}".format(file_no_ext, file_id, file_ext)
    path = path / full_file_name

    urllib.request.urlretrieve(file_link, path)

