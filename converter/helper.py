import os
import time
import random


def storage_path(name: str):
    return "storage/" + name


def generate_file_name(postscript):
    return str(random.randint(1, 100)) + "_" + str(int(time.time())) + "_" + postscript


def del_temporary_files(name):
    for filename in os.listdir(storage_path("")):
        if filename.startswith(name):
            os.remove(os.path.join(storage_path(filename)))
