import requests
from bs4 import BeautifulSoup
import os


ROOT_URL = "https://www.cs.cmu.edu/afs/cs/academic/class/15213-f19/www/code/"
ROOT_DIR = "/Users/Armstrong/Dropbox/Scripts/15213-code-download/data/"


def gen_sub_url_ref(endpoint=""):
    url = ROOT_URL+endpoint
    file_path = ROOT_DIR+endpoint

    # base case: if it's a file, save to file
    if url[-1] != "/":
        save_to_file(url, file_path)
        return

    # if not file, get file/subdir list, recurse
    response = requests.get(url)
    sub_soup = BeautifulSoup(response.text, "lxml-xml")
    a_ref_ls = sub_soup.find_all("a")
    a_ref_text_ls = [a.text for a in a_ref_ls]
    parent_dir_index = a_ref_text_ls.index("Parent Directory")
    for sub in [a["href"] for a in a_ref_ls[parent_dir_index+1:]]:
        gen_sub_url_ref(endpoint+sub)


def save_to_file(url, file_path):
    response = requests.get(url)
    dir_ls = file_path.split("/")
    dir_ls.pop()
    os.makedirs("/".join(dir_ls), exist_ok=True)
    with open(file_path, "wb") as file:
        file.write(response.content)


def main():
    gen_sub_url_ref()


if __name__ == "__main__":
    main()
