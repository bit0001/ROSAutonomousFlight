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
        window.resizable(width=FALSE, height=FALSE)
        self.change_window_size(window, 500, 400)

        top_frame = Frame(window)
        top_frame.pack()
        below_top_frame = Frame(window)
        below_top_frame.pack()
        middle_frame = Frame(window)
        middle_frame.pack()
        bottom_frame = Frame(window)
        bottom_frame.pack()

        window.title("Thesis Interface")

        drone_image = PhotoImage(file='./ardrone.gif')
        display_drone_image = drone_image.subsample(2, 2)

        label = Label(below_top_frame, image=drone_image).pack(side=LEFT)

        title_label = Label(top_frame, text="GUI for ARDrone Autonomous Flight", font="bold")
        title_label.pack()
        save_files_button = Button(middle_frame, text="Save attached files", command=self.get_files_from_email)
        save_files_button.pack(side=LEFT)
        ros_start_button = Button(middle_frame, text="Start ROS", command=self.start_ROS)
        ros_start_button.pack(side=LEFT)
        follow_trajectory_button = Button(middle_frame, text="Follow Trajectory", command=self.follow_trajectory)
        follow_trajectory_button.pack(side=LEFT)
        plot_results_button = Button(bottom_frame, text="Plot Results", command=self.plot_results)
        plot_results_button.pack()

        window.mainloop()  # Create an event loop

    def start_ROS(self):
        os.system("bash start_ROS.sh &")

    def get_files_from_email(self):
        subprocess.call("python3 save_references.py 1", shell=True)

    def follow_trajectory(self):
        subprocess.call("python3 main.py 1", shell=True)

    def plot_results(self):
        subprocess.call("python3 plot_results.py 1 &", shell=True)

    def change_window_size(self, window, width, height):
        window.geometry('{}x{}'.format(width, height))


ROSLauncher()
