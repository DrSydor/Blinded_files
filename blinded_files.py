'''
A script to blind the files in a directory for analysis. Ensure that this 
script is placed in the original directory with the original files to be 
blinded. It is non-destructive and will create a copy of the files to be
blinded and record their identities to a text file.
'''

from pathlib import Path
import shutil, os
import random

suffix = input("What is the file extension of the files you want to blind? ")

#list the contents of the current directory 
directory = os.listdir()
random.shuffle(directory)   #shuffle the directory list
directory.remove("Blinding.py")
dir_len = len(directory)

#create a folder for the blinded files
cwd = Path.cwd()
(cwd / 'blinded').mkdir(parents=True)

#create a random list with the same number of elements as the directory
blind_file_num1 = random.sample(range(1, (dir_len * 20)), dir_len)
blind_name = ["blindfile_" + str(s) for s in blind_file_num1]

# Creating a new text file for outputting the results
my_file = open("Blinded Files Log.txt", "w")
my_file.write("The identity of the blinded files are as follows:\n\n")

#copy the files and assign a random name; log the old and new names to a .txt file
n = 0
for file in directory:
    name = ".\\" + file
    blind_directory = ".\\blinded\\" + blind_name[n] + suffix
    shutil.copy(name, blind_directory)
    my_file.write(blind_name[n] + ", " + file + "\n")
    n += 1
    
my_file.close()
