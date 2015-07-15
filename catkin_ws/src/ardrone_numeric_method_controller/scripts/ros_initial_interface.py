#!/usr/bin/python3
"""
This is a small interface that initializes the ROS interface.
"""
from tkinter import *
import os
import subprocess


# Import all definitions from tkinter
class ROSLauncher:
    def __init__(self):
        window = Tk()
        window.title("Thesis Interface")
        window.resizable(width=FALSE, height=FALSE)
        self.change_window_size(window, 500, 350)

        top_frame = Frame(window)
        top_frame.pack()
        image_frame = Frame(window)
        image_frame.pack()
        middle_frame = Frame(window)
        middle_frame.pack()
        bottom_frame = Frame(window)
        bottom_frame.pack()

        title_label = Label(top_frame, text="GUI for ARDrone Autonomous Flight", font="bold")
        title_label.pack()

        self.insert_spaces_in_frame(top_frame, 1)

        drone_image = PhotoImage(file='./ardrone.gif')
        image_label = Label(image_frame, image=drone_image)
        image_label.pack(side=LEFT)

        self.insert_spaces_in_frame(middle_frame, 1)

        save_files_button = Button(middle_frame, text="Save Attached Files", command=self.get_files_from_email)
        save_files_button.pack(side=LEFT)
        ros_start_button = Button(middle_frame, text="Start ROS", command=self.start_ROS)
        ros_start_button.pack(side=LEFT)
        draw_trajectory_button = Button(middle_frame, text="Draw Trajectory", command=self.draw_trajectory)
        draw_trajectory_button.pack(side=LEFT)
        follow_trajectory_button = Button(bottom_frame, text="Follow Trajectory", command=self.follow_trajectory)
        follow_trajectory_button.pack(side=LEFT)
        plot_results_button = Button(bottom_frame, text="Plot Results", command=self.plot_results)
        plot_results_button.pack()


        window.mainloop()

    def start_ROS(self):
        os.system("bash start_ROS.sh &")

    def get_files_from_email(self):
        subprocess.call("python3 save_references.py 1", shell=True)

    def draw_trajectory(self):
        subprocess.call("python3 draw_trajectory.py 1", shell=True)

    def follow_trajectory(self):
        subprocess.call("python3 main.py 1", shell=True)

    def plot_results(self):
        subprocess.call("python3 plot_results.py 1 &", shell=True)

    def change_window_size(self, window, width, height):
        window.geometry('{}x{}'.format(width, height))

    def insert_spaces_in_frame(self, frame, spaces):
        for i in range(spaces):
            blank_label = Label(frame, text=" ")
            blank_label.pack()


ROSLauncher()
