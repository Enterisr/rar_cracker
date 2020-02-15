from zipfile import ZipFile
from datetime import datetime
import os
from threading  import Thread #TODO: CHNAGE TO PROCSSES LIB, THATS NOT REALLY SPEEDS THE PROGRAM 
import shutil
from rarfile import RarFile


def extract(password, file_name="example.rar"):
    time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    path = "~/extraction/"+time
    with RarFile(file_name, 'r') as rar:
        try:
            rar.extractall(path=path, pwd=password.encode())
            print(password + " is the password")
            return True
        except:
            print(password + "is not the password")

          #  shutil.rmtree("~/extraction/"+time)  # Delete..
            return False

def search(words_list):
    for line in words_list:
        p = line.replace('\n', '')
        if extract(p):
            return True
        elif not p.islower():
            lower_p = p.lower()
            if extract(lower_p):
                return True

def start(threadNumber=10):
    with open('words.txt', 'r') as dictionary:
        all_words = dictionary.readlines()   
        all_words_sections = []
        section_size = round(len(all_words)/threadNumber)
        for thread_idx in range(threadNumber):
            words_index = section_size*thread_idx
            words_index_limit = section_size*(thread_idx+1)
            all_words_sections.append(all_words[words_index:words_index_limit])
            t = Thread()

if __name__ == "__main__": 
    start(10)

