#!/usr/bin/python3
"""
This is a small interface that initializes the ROS interface.
"""
from tkinter import *
import os
import subprocess

PATH_TO_SCRIPTS = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/" \
                  "ardrone_numeric_method_controller/scripts/"


class ROSLauncher:
    def __init__(self):
        window = Tk()
        window.title("Thesis Interface")
        window.resizable(width=FALSE, height=FALSE)
        self.change_window_size(window, 500, 400)

        top_frame = Frame(window)
        top_frame.pack()
        image_frame = Frame(window)
        image_frame.pack()
        middle_frame = Frame(window)
        middle_frame.pack()
        bottom_frame = Frame(window)
        bottom_frame.pack()
        foot_frame = Frame(window)
        foot_frame.pack()

        title_label = Label(top_frame, text="GUI for ARDrone Autonomous Flight", font="TkDefaultFont 15 bold")
        title_label.pack()
        self.insert_spaces_in_frame(top_frame, 2)

        drone_image = PhotoImage(file=PATH_TO_SCRIPTS + "/ardrone.gif")
        image_label = Label(image_frame, image=drone_image)
        image_label.pack(side=LEFT)

        self.insert_spaces_in_frame(middle_frame, 2)

        save_files_button = Button(middle_frame, text="Save Attached Files", command=self.get_files_from_email)
        save_files_button.pack(side=LEFT)
        ros_start_button = Button(middle_frame, text="Start ROS", command=self.start_ROS)
        ros_start_button.pack(side=LEFT)
        draw_trajectory_button = Button(middle_frame, text="Draw Trajectory", command=self.draw_trajectory)
        draw_trajectory_button.pack(side=LEFT)
        # follow_trajectory_button = Button(bottom_frame, text="Follow Trajectory", command=self.follow_trajectory)
        # follow_trajectory_button.pack(side=LEFT)
        plot_results_button = Button(middle_frame, text="Plot Results", command=self.plot_results)
        plot_results_button.pack()
        self.insert_spaces_in_frame(foot_frame, 1)
        foot_note = Label(foot_frame, text="© 2015 EPN All Rights Reserved")
        foot_note.pack()

        window.mainloop()

    def start_ROS(self):
        os.system("bash " + PATH_TO_SCRIPTS + "start_ROS.sh &")

    def get_files_from_email(self):
        subprocess.call("python3 " + PATH_TO_SCRIPTS + "save_references.py 1", shell=True)

    def draw_trajectory(self):
        subprocess.call("python3 " + PATH_TO_SCRIPTS + "draw_trajectory.py 1 &", shell=True)

    def follow_trajectory(self):
        subprocess.call("python3 " + PATH_TO_SCRIPTS + "main.py 1 &", shell=True)

    def plot_results(self):
        subprocess.call("python3 " + PATH_TO_SCRIPTS + "plot_results.py 1 &", shell=True)

    def change_window_size(self, window, width, height):
        window.geometry('{}x{}'.format(width, height))

    def insert_spaces_in_frame(self, frame, spaces):
        for i in range(spaces):
            blank_label = Label(frame, text=" ")
            blank_label.pack()


ROSLauncher()
