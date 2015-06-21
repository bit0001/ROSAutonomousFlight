#!/usr/bin/env python

"""This is a module that contains useful functions for this project."""


def get_array_from_file(path_to_file):
    with open(path_to_file) as opened_file:
        content = opened_file.read()
    return content.split('\n')[:-1]


def save_array_into_file(array, path_to_file):
    created_file = open(path_to_file, 'w+')

    for item in array:
        created_file.write("%s\n" % item)
