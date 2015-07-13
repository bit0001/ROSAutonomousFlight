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
        self.change_window_size(window, 400, 100)

        top_frame = Frame(window)
        top_frame.pack()
        bottom_frame = Frame(window)
        bottom_frame.pack()


        window.title("Thesis Interface")


        label = Label(top_frame, text="GUI for ARDrone Autonomous Flight")
        label.pack()
        save_files_button = Button(bottom_frame, text="Save attached files", command=self.get_files_from_email)
        save_files_button.pack(side=LEFT)
        ros_start_button = Button(bottom_frame, text="Start ROS", command=self.start_ROS)
        ros_start_button.pack(side=LEFT)
        follow_trajectory_button = Button(bottom_frame, text="Follow Trajectory", command=self.get_files_from_email)
        follow_trajectory_button.pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def start_ROS(self):
        os.system("bash start_ROS.sh &")

    def get_files_from_email(self):
        subprocess.call("python3 save_references.py 1", shell=True)

    def get_files_from_email(self):
        subprocess.call("python3 main.py 1", shell=True)

    def change_window_size(self, window, width, height):
        window.geometry('{}x{}'.format(width, height))

ROSLauncher()
