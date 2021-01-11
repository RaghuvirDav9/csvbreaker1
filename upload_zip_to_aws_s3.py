import boto3
from zipfile import ZipFile
import os
import typing

s3 = boto3.resource('s3')
BUCKET = "lambda-demo12"


# This function takes directory as an input and creates a list with full path of every file in the given directory
def get_all_file_paths(directory) -> list:
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


""" This function in the initial function which calls get_all_file_paths() fun 
    and performs zip on received object in list and uploads zip to aws"""


def main() -> None:
    directory = './lambda'
    file_paths = get_all_file_paths(directory)
    with ZipFile('my_python.zip', 'w') as zip:
        for file in file_paths:
            zip.write(file)
    s3.Bucket(BUCKET).upload_file("./my_python.zip", "lambda/")


if __name__ == "__main__":
    main()
