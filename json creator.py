import os
import sys

alph="abcdefghijklmnopqrstuvwxyz"

def filename(letter):
    name = "database/targhe"+letter.upper()+".json"
    return name


for letter in alph:

    os.system('echo "{\n}">'+filename(letter))

print 'done'