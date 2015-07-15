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


def get_float_list_from_txt_file(txt_file):
    return string_list_to_float_list(get_list_from_file(txt_file + ".txt"))


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


def encode_string_to_binary(string):
    return string.encode(encoding='UTF-8')


def reduce_points_in_attached_binary_file(attachment, max_length, hysteresis):
    string_list = convert_bin_file_to_string_list(attachment[1])
    float_list = string_list_to_float_list(string_list)
    reduced_float_list = reduce_list_until_be_useful(float_list, max_length, hysteresis)
    string_to_save = float_list_to_string(reduced_float_list)
    encoded_string = encode_string_to_binary(string_to_save)

    return encoded_string


def save_attached_files_from_email(host, user, password, path_to_save_files):
    last_received_email = easyimap.connect(host, user, password).listup()[0]

    for attachment in last_received_email.attachments:
        with open(path_to_save_files + attachment[0], 'bw+') as f:
            reduced_binary_file = reduce_points_in_attached_binary_file(attachment, 101, 5)
            f.write(reduced_binary_file)


def save_list_into_txt(a_list, txt_file):
    save_list_into_file(a_list, txt_file + '.txt')


def show_legend(figure):
    legend = figure.legend(loc="best", shadow=True)

    for label in legend.get_texts():
        label.set_fontsize("medium")

    for label in legend.get_lines():
        label.set_linewidth(1.0)


def plot_reference_and_position(figure, reference, position, time):
    figure.plot(time, position, "b", label="Actual")
    figure.plot(time, reference, "r--", label="Reference")


def add_title_and_axis_labels(figure, title, x_label, y_label):
    figure.set_title(title)
    figure.set_xlabel(x_label)
    figure.set_ylabel(y_label)


def plot_errors(figure, error, time):
    zeros = [0 for e in range(len(error))]
    figure.plot(time, error, "b")
    figure.plot(time, zeros, "r--")
