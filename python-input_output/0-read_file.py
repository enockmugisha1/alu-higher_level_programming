#!/usr/bin/python3

def read_file(filename=""):
    with open("file.xt", "r", encoding = 'UTF8') as p:
        print(p.read())

