import os
from bs4 import BeautifulSoup
import re

def creatmaindic(flderwithdata): #the argument is the name of folder + /

    maindic = {}

    #going file by file with every file from main folder
    list_files = os.listdir(flderwithdata)

    for years in list_files:

        #extrapolating years from file name with regex
        numbers = re.sub(r"\D", "", years)

        #adding keys to our main dict where keys will be the years of file
        maindic[numbers] = []

        #using the beautifulsub lib to clean the data, we are adding every sentence as a list of strings to value in main dict
        with open(flderwithdata + years, 'r') as f:
            readable = f.read()
            soup = BeautifulSoup(readable, 'html.parser')
            sentences = soup.find_all('sentence')

            #TRESHOLD ONLY 10 SENTENCES BETWEEN 10 AND 20
            for sentence in sentences:#[10:20]:

                list_sent = []
                for word in sentence.get_text().split("\n")[1:]:
                    list_sent.append(word.split("\t")[0])
                maindic[numbers].append(list_sent)
    return maindic

print(creatmaindic("vrt/"))

