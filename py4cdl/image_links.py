import bs4


def get_image_links_and_names(page):

    image_links_and_names = []

    soup = bs4.BeautifulSoup(page, "html.parser")

    for media_post in soup.find_all("div", class_="fileText"):
        for link in media_post.find_all("a"):
            link_file = "https:" + link.get("href")
            link_name = link.get("title")
            link_id = link_file.split("/")[-1].split(".")[0]
            # Some don't have a title, so we fall back to text
            if link_name is None:
                link_name = link.text

            image_links_and_names.append((link_file, link_name, link_id))

    return image_links_and_names

