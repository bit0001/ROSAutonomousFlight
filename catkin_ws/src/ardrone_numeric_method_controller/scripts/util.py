#!/usr/bin/env python

"""This is a module that contains useful functions for this project."""
import easyimap
import imaplib
import random
import math
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
            MAX_LENGTH = 101
            string_attachment = attachment[1].decode(encoding='UTF-8')
            list_attachment = string_attachment.split("\n")[:-1]

            float_attachment_list = []

            for e in list_attachment:
                float_attachment_list.append(float(e))

            if len(float_attachment_list) > MAX_LENGTH:
                float_attachment_list = reduce_list_until_be_useful(float_attachment_list, MAX_LENGTH, 5)

            string_to_save = ''
            for item in float_attachment_list:
                string_to_save += str(item) + '\n'

            f.write(string_to_save.encode(encoding='UTF-8'))

def reduce_points(list_to_reduce, max_length):
    additional_points = len(list_to_reduce) - max_length
    new_random_list = []

    for index in range(len(list_to_reduce)):
        if index % (int(len(list_to_reduce) / additional_points) + 1) != 0:
            new_random_list.append(list_to_reduce[index])

    return new_random_list

def reduce_list_until_be_useful(list_to_reduce, max_length, hysteresis):
    while abs(len(list_to_reduce) - max_length) >= hysteresis:
        list_to_reduce = reduce_points(list_to_reduce, max_length)

    return list_to_reduce



if __name__ == "__main__":
    MAX_LENGTH = 101
    lengths = []

    for i in range(1000):
        randomLength = random.randint(90, 200)
        randomList = random.sample(range(1000), randomLength)

        print("The length is " + str(randomLength))

        if len(randomList) <= MAX_LENGTH:
            print("The arrays remains the same.", len(randomList))
        else:
            randomList = reduce_list_until_be_useful(randomList, MAX_LENGTH, 5)

        lengths.append(len(randomList))
        print("The array has changed")
        print("\t", "New length:", len(randomList))
        lengths.append(len(randomList))

    print("Lengths", lengths)
    print("Max length", max(lengths))
    print("Min Length", min(lengths))
