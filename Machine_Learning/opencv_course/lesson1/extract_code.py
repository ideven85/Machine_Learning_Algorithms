import os
from urllib.request import urlretrieve
import zipfile

import requests

def download_and_extract(url,save_path):

    #file_name=requests.get(url)
    urlretrieve(url,save_path)
    # if not file_name:
    #     return
    file_name = save_path.split("/")[-1]
    print(file_name)

    with zipfile.ZipFile(file_name, "r") as zip_ref:
            zip_ref.extractall(os.path.split(save_path)[0])









def main():
    URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"
    images_path = os.getcwd() + "/images/opencv_bootcamp_assets_NB1.zip"
    if not os.path.exists(images_path):
        download_and_extract(URL,images_path)


if __name__ == '__main__':
    main()