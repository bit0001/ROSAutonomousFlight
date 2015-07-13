#!/usr/bin/python3

"""This is a module that contains useful functions for this project."""
import imaplib

import easyimap

imaplib._MAXLINE = 100000


def get_list_from_file(path_to_file):
    with open(path_to_file) as opened_file:
        content = opened_file.read()
    return content.split('\n')[:-1]


def string_list_to_float_list(string_array):
    float_list = []
    for item in string_array:
        float_list.append(float(item))

    return float_list


def save_list_into_file(a_list, path_to_file):
    created_file = open(path_to_file, 'w+')

    for item in a_list:
        created_file.write("%s\n" % item)


def reduce_points(list_to_reduce, max_length):
    additional_points = len(list_to_reduce) - max_length
    new_random_list = []

    for index in range(len(list_to_reduce)):
        if index % (int(len(list_to_reduce) / additional_points) + 1) != 0:
            new_random_list.append(list_to_reduce[index])

    return new_random_list


def reduce_list_until_be_useful(list_to_reduce, max_length, hysteresis):
    if len(list_to_reduce) > max_length:
        while abs(len(list_to_reduce) - max_length) >= hysteresis:
            list_to_reduce = reduce_points(list_to_reduce, max_length)

    return list_to_reduce


def convert_bin_file_to_string_list(bin_file):
    return bin_file.decode(encoding='UTF-8').split("\n")[:-1]


def float_list_to_string(float_attachment_list):
    string_to_save = ''
    for item in float_attachment_list:
        string_to_save += str(item) + '\n'
    return string_to_save


def save_attached_files_from_email(host, user, password, path_to_save_files):
    imapper = easyimap.connect(host, user, password)

    last_received_email = imapper.listup()[0]

    for attachment in last_received_email.attachments:
        with open(path_to_save_files + attachment[0], 'bw+') as f:
            MAX_LENGTH = 101
            list_attachment = convert_bin_file_to_string_list(attachment[1])
            float_attachment_list = string_list_to_float_list(list_attachment)

            float_attachment_list = reduce_list_until_be_useful(float_attachment_list, MAX_LENGTH, 5)

            string_to_save = float_list_to_string(float_attachment_list)

            f.write(string_to_save.encode(encoding='UTF-8'))
