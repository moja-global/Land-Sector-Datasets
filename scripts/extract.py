import argparse
import requests
import zipfile
import io
import os

#URL = "https://databasin2-filestore.s3.amazonaws.com:443/a4cb6d367eae4e52a08902874f8bfedf/download/a4cb6d367eae4e52a08902874f8bfedf_1_zip_en.zip?Signature=O6QSoOR%2BisIRVE2mpxzkphTkhmw%3D&Expires=1680100356&AWSAccessKeyId=AKIAI4RK5BEPK3FCQPUQ"
URL = "https://zenodo.org/record/5848610/files/biome_cluster_shapefile.zip?download=1"
def ensure_url_is_accessible(URL):
    r = requests.get(URL)
    if not r.ok:
        print("Download link expired. Please update download link")
    else:
        download_and_unzip_files(r.content)

def download_and_unzip_files(content):
    current_directory = os.getcwd()
    target_parent_dir = os.path.join(current_directory, r'tmp_unzip_path')
    if not os.path.exists(target_parent_dir):
        os.mkdir(target_parent_dir)
    try:
        z = zipfile.ZipFile(io.BytesIO(content))
        z.extractall(target_parent_dir)
    except Exception as e:
        print(e)
    else:
        print("unzipped successfully")

ensure_url_is_accessible(URL)