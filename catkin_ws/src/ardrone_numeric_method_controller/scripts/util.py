#!/usr/bin/env python

"""This is a module that contains useful functions for this project."""
import easyimap
import imaplib
imaplib._MAXLINE = 100000

def get_list_from_file(path_to_file):
    with open(path_to_file) as opened_file:
        content = opened_file.read()
    return content.split('\n')[:-1]


def save_list_into_file(a_list, path_to_file):
    created_file = open(path_to_file, 'w+')

    for item in a_list:
        created_file.write("%s\n" % item)

def save_attached_files_from_email(host, user, password, path_to_save_files):
    imapper = easyimap.connect(host, user, password)

    last_received_email = imapper.listup()[0]

    for attachment in last_received_email.attachments:
        with open(path_to_save_files + attachment[0], 'bw+') as f:
            f.write(attachment[1])
